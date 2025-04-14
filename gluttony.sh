#!/bin/bash
# Gluttony - A simple script to install and configure the stack on Ubuntu



sudo apt -y update
sudo apt -y full-upgrade

# Configure device interfaces
#turn on i2c
sudo raspi-config nonint do_i2c 0
#turn on spi
sudo raspi-config nonint do_spi 0
#turn on serial
sudo raspi-config nonint do_serial 0
#turn on 1-wire
sudo raspi-config nonint do_onewire 0
#turn on camera
sudo raspi-config nonint do_camera 0


#install git
sudo apt install -y git

#install raspberry pi connect
sudo apt install -y rpi-connect

#install i2c tools
sudo apt install -y i2c-tools

#install python3 venv
sudo apt-get install -y python3-venv

#install python3 pip
sudo apt install -y python3-pip

# Set env variables
read -p "Enter your Google Maps API Key: " GOOGLE_MAPS_API_KEY
export GOOGLE_MAPS_API_KEY
if ! grep -q "export GOOGLE_MAPS_API_KEY=" ~/.bashrc; then
    echo "export GOOGLE_MAPS_API_KEY=$GOOGLE_MAPS_API_KEY" >> ~/.bashrc
fi



#git clone the gluttony repo
cd ~
git clone 

python3 -m venv .venv

source myenv/bin/activate
pip install -r requirements.txt


