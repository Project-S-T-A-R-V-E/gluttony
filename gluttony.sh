#!/bin/bash
# Gluttony - A script to install and configure the stack on Raspberry Pi

# Update and upgrade the system
sudo apt -y update
sudo apt -y full-upgrade

# Configure device interfaces using raspi-config
echo "Configuring Raspberry Pi interfaces..."
sudo raspi-config nonint do_i2c 0       # Enable I2C
sudo raspi-config nonint do_spi 0       # Enable SPI
sudo raspi-config nonint do_serial 0    # Enable Serial
sudo raspi-config nonint do_onewire 0   # Enable 1-Wire
sudo raspi-config nonint do_camera 0    # Enable Camera

# Install essential packages
echo "Installing essential packages..."
sudo apt install -y git                 # Install Git
sudo apt install -y rpi-connect         # Install Raspberry Pi Connect
sudo apt install -y i2c-tools           # Install I2C tools
sudo apt install -y python3-venv        # Install Python virtual environment
sudo apt install -y python3-pip         # Install Python pip
sudo apt install -y libatlas-base-dev   # Install dependencies for numpy/scipy
sudo apt install -y libopenjp2-7 libtiff5 # Install image processing libraries (if needed)

# Set environment variables
echo "Setting up environment variables..."
read -p "Enter your Google Maps API Key: " GOOGLE_MAPS_API_KEY
export GOOGLE_MAPS_API_KEY
if ! grep -q "export GOOGLE_MAPS_API_KEY=" ~/.bashrc; then
    echo "export GOOGLE_MAPS_API_KEY=$GOOGLE_MAPS_API_KEY" >> ~/.bashrc
fi

# Create and activate Python virtual environment
echo "Creating Python virtual environment..."
python3 -m venv .venv
source .venv/bin/activate

# Install required Python packages
echo "Installing Python dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

# Install npm and Socket.IO (if needed)
echo "Installing npm and Socket.IO..."
sudo apt install -y npm
npm install socket.io

# Install ngrok (for exposing localhost)
echo "Installing ngrok..."
wget https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-linux-arm64.tgz
tar -xvzf ngrok-v3-stable-linux-arm64.tgz
sudo mv ngrok /usr/local/bin
rm ngrok-v3-stable-linux-arm64.tgz

# Verify I2C devices
echo "Verifying I2C devices..."
i2cdetect -y 1

# Final message
echo "Setup complete! Please reboot your Raspberry Pi to apply all changes."