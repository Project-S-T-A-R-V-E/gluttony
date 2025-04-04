from socket import socket
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
socket = SocketIO(app, cors_allowed_origins="*")
print ("Flask SocketIO initialized")

# Main page
# export GOOGLE_MAPS_API_KEY="your_api_key_here"
@app.route("/")
def main():
    api_key = os.getenv("GOOGLE_MAPS_API_KEY")
    print("server started")
# Dynamically get the host IP address
    server_ip = socket.gethostbyname(socket.gethostname())
    return render_template("STARVE.html", api_key=api_key, server_ip=server_ip)    

# WebSocket Events

@socket.on('connect')
def handleConnect():
    print("WebSocket connected")

@socket.on('disconnect')
def handleDisconnect():
    print("WebSocket disconnected")

@socket.on('message')
def handleMsg(msg):
    # Step 1: Send Sensor Data over WebSocket
    socket.send([env.getVoltage(), 
                 env.getTemp(), 
                 env.getHumidity(),
                 imu.getPYR()[0], imu.getPYR()[1], imu.getPYR()[2], 
                 imu.getAccelXYZ()[0], imu.getAccelXYZ()[1], imu.getAccelXYZ()[2], 
                 imu.getMagXYZ()[0], imu.getMagXYZ()[1], imu.getMagXYZ()[2],
                #  gps.getGPS()[0],gps.getGPS()[1],
                 rangeFinder.getRangeFinder()])
    print ("Message Received: " + msg)

# Start Flask Server w/ Socketio
if __name__ == "__main__":
    socket.run(app, host= '0.0.0.0', port=5000)
    # socket.send("go")
