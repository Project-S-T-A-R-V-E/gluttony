# Installation Steps (Linux Machines Only)  
1. **Create and Activate Virtual Environment**  
      ```bash
      python3 -m venv venv
      source venv/bin/activate
      ```

2. **Install Required Python Packages**  
    ```bash
    pip install -r requirements.txt
    ```

3. **Install npm and Socket.IO**  
    ```bash
    sudo apt install npm
    npm install socket.io
    ```

4. **Google Maps API Key**  
    For the Google Maps API key, please contact [etjoy1@morgan.edu](mailto:etjoy1@morgan.edu).

5. **Start ngrok on Port 5000**  
    ```bash
    ngrok http 5000
    ```

6. ## Run the Python Script
    ```bash
    sudo python3 main.py
    ```

## Resource
- [How to use Raspberry Pi GPIO pins with Ubuntu](https://ubuntu.com/tutorials/gpio-on-raspberry-pi)
- [How to Use NEO 6M GPS with RPI (Begginer Friendly)](https://www.geekering.com/categories/embedded-sytems/raspberry-pi/rubenmarques/how-to-use-neo-6m-gps-with-rpi-begginer-friendly/)
- [How to control a servo motor with Raspberry Pi and servo driver "PCA9685"](https://python-academia.com/en/raspberrypi-pca9685-servo/)
- [Adafruit ServoKit Library](https://docs.circuitpython.org/projects/servokit/en/latest/)
- [Miniature Linear Motion Series · L12](https://www.actuonix.com/assets/images/datasheets/ActuonixL12Datasheet.pdf)
- [Raspberry Pi Tutorial: How to Use the DHT-22](https://www.instructables.com/Raspberry-Pi-Tutorial-How-to-Use-the-DHT-22/)
- [icm20948-python/](https://github.com/pimoroni/icm20948-python/tree/main)