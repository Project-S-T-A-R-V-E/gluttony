import smbus
import time

# Define I2C address and register
I2C_ADDRESS = 0x10  # Replace with correct address if needed
REGISTER_DISTANCE = 0x00  # Register for distance data

# Initialize I2C bus
bus = smbus.SMBus(1)  # Use 0 for older Raspberry Pi models

def read_distance():
    """ Read distance measurement from TF-Luna via I2C """
    try:
        data = bus.read_i2c_block_data(I2C_ADDRESS, REGISTER_DISTANCE, 2)
        distance = data[0] | (data[1] << 8)  # Combine low and high bytes
        return distance
    except Exception as e:
        print(f"Error reading distance: {e}")
        return None

# Continuously read and display distance
#while True:
#   dist = read_distance()
#    if dist is not None:
#       print(f"Distance: {dist} cm")
#   time.sleep(0.5)
