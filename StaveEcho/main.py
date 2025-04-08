import socket  # Import the standard library socket module
from flask_socketio import SocketIO
from flask import Flask, render_template
import time
import envSensor as env 
import imu
import gps
import rangeFinder
import os
import asyncio

voltage = 0
internal_temp = 0
internal_humidity = 0
external_temp = 0
external_humidity = 0
pyr_x = 0
pyr_y = 0
pyr_z = 0
accel_x = 0
accel_y = 0
accel_z = 0
mag_x = 0
mag_y = 0
mag_z = 0
gps_lat = 0
gps_lon = 0
range_finder = 0


# Flask Set up
app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")  # Rename this variable to avoid conflict
print("Flask SocketIO initialized")
server_ip = "192.168.1.45"  # Use the standard library socket module

# Main page
@app.route("/")
def main():
    api_key = os.getenv("GOOGLE_MAPS_API_KEY")
    print("server started")
    # Dynamically get the host IP address
    server_ip = socket.gethostbyname(socket.gethostname())  # Use the standard library socket module
    # print("Server IP Address: " + server_ip)
    return render_template("STARVE.html", api_key=api_key, server_ip=server_ip)

# WebSocket Events
@socketio.on('connect')
def handleConnect():
    print("WebSocket connected")

@socketio.on('disconnect')
def handleDisconnect():
    print("WebSocket disconnected")

@socketio.on('message')
def handleMsg(msg):
    # Step 1: Send Sensor Data over WebSocket
    socketio.send([voltage, 
                   internal_temp, internal_humidity,
                   external_temp, external_humidity,
                   pyr_x, pyr_y, pyr_z, 
                   accel_x, accel_y, accel_z, 
                   mag_x, mag_y, mag_z,
                   gps_lat, gps_lon,
                   range_finder])
    # print("Message Received: " + msg)

# Start Flask Server w/ SocketIO
if __name__ == "__main__":
    socketio.run(app, host=server_ip, port=5000)

# Async updates
async def update_voltage():
    global voltage
    while True:
        voltage = env.getVoltage()
        await asyncio.sleep(0.1)

async def update_internal_temp():
    global internal_temp
    while True:
        internal_temp = env.getInternalTemp()
        await asyncio.sleep(0.1)

async def update_internal_humidity():
    global internal_humidity
    while True:
        internal_humidity = env.getInternalHumidity()
        await asyncio.sleep(0.1)

async def update_external_temp():
    global external_temp
    while True:
        external_temp = env.getExternalTemp()
        await asyncio.sleep(0.1)

async def update_external_humidity():
    global external_humidity
    while True:
        external_humidity = env.getExternalHumidity()
        await asyncio.sleep(0.1)

async def update_imu():
    global pyr_x, pyr_y, pyr_z, accel_x, accel_y, accel_z, mag_x, mag_y, mag_z
    while True:
        pyr_x, pyr_y, pyr_z = imu.getPYR()
        accel_x, accel_y, accel_z = imu.getAccelXYZ()
        mag_x, mag_y, mag_z = imu.getMagXYZ()
        await asyncio.sleep(0.1)

async def update_gps():
    global gps_lat, gps_lon
    while True:
        gps_lat, gps_lon = gps.getGPS()
        await asyncio.sleep(2)



# Run both coroutines concurrently
async def main():
    await asyncio.gather(
        update_voltage(),
        update_internal_temp(),
        update_internal_humidity(),
        update_external_temp(),
        update_external_humidity(),
        update_imu(),
        update_gps()
    )
    print("sensors updated")

asyncio.run(main())