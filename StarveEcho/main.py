import socket  # Import the standard library socket module
from flask import Flask, render_template, Response
from flask_socketio import SocketIO
from picamera2 import Picamera2
import cv2
import time
import os
import asyncio
import envSensor as env
import imu
import gps
import rangeFinder
import motorControl as mc

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
socketio = SocketIO(app, cors_allowed_origins="*")

# Initialize the Raspberry Pi Camera
picam2 = Picamera2()
picam2.configure(picam2.create_video_configuration(main={"size": (640, 480)}))
picam2.start()

# Camera feed generator
def generate_camera_feed():
    while True:
        frame = picam2.capture_array()
        _, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
        time.sleep(0.1)  # Adjust frame rate if needed

# Route for the camera feed
@app.route('/video_feed')
def video_feed():
    return Response(generate_camera_feed(), mimetype='multipart/x-mixed-replace; boundary=frame')

# Main page
@app.route("/")
def main():
    api_key = os.getenv("GOOGLE_MAPS_API_KEY")
    print("server started")
    # Dynamically get the host IP address
    server_ip = socket.gethostbyname(socket.gethostname())  # Use the standard library socket module
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
    if msg == "Controller Connected":
        socketio.send([voltage, 
                   internal_temp, internal_humidity,
                   external_temp, external_humidity,
                   pyr_x, pyr_y, pyr_z, 
                   accel_x, accel_y, accel_z, 
                   mag_x, mag_y, mag_z,
                   gps_lat, gps_lon,
                   range_finder])
    else:
        mc.drive(msg[0],msg[1])
        mc.actuation(msg[2],msg[3],msg[4],msg[5])
        socketio.send([voltage, 
                   internal_temp, internal_humidity,
                   external_temp, external_humidity,
                   pyr_x, pyr_y, pyr_z, 
                   accel_x, accel_y, accel_z, 
                   mag_x, mag_y, mag_z,
                   gps_lat, gps_lon,
                   range_finder])

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
        pyr_x, pyr_y, pyr_z, accel_x, accel_y, accel_z, mag_x, mag_y, mag_z = imu.getIMU()
        await asyncio.sleep(0.4)

async def update_gps():
    global gps_lat, gps_lon
    while True:
        new_lat, new_lon = gps.getGPS()
        if new_lat is not None and new_lon is not None:
            gps_lat, gps_lon = new_lat, new_lon
        await asyncio.sleep(60)

async def update_rangefinder():
    global range_finder
    while True:
        range_finder = rangeFinder.getLidarData()
        await asyncio.sleep(5)

# Run both coroutines concurrently
async def updateAllSensors():
    await asyncio.gather(
        update_voltage(),
        update_internal_temp(),
        update_internal_humidity(),
        update_external_temp(),
        update_external_humidity(),
        update_imu(),
        update_gps(),
        update_rangefinder()
    )

# Start Flask Server w/ SocketIO
if __name__ == "__main__":
    # Start the async tasks in a separate thread
    def start_async_tasks():
        asyncio.run(updateAllSensors())

    from threading import Thread
    Thread(target=start_async_tasks, daemon=True).start()

    # Run the Flask-SocketIO server
    socketio.run(app, host="0.0.0.0", port=5000)