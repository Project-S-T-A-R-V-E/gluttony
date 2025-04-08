import socket  # Import the standard library socket module
from flask_socketio import SocketIO
from flask import Flask, render_template
import time
import envSensor as env 
import imu
import gps
import rangeFinder
import os

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
    socketio.send([env.getVoltage(), 
                   env.getInternalTemp(), env.getInternalHumidity(),
                   env.getExternalTemp(), env.getExternalHumidity(),
                   imu.getPYR()[0], imu.getPYR()[1], imu.getPYR()[2], 
                   imu.getAccelXYZ()[0], imu.getAccelXYZ()[1], imu.getAccelXYZ()[2], 
                   imu.getMagXYZ()[0], imu.getMagXYZ()[1], imu.getMagXYZ()[2],
                   gps.getGPS()[0], gps.getGPS()[1],
                   rangeFinder.getRangeFinder()])
    # print("Message Received: " + msg)

# Start Flask Server w/ SocketIO
if __name__ == "__main__":
    socketio.run(app, host=server_ip, port=5000)