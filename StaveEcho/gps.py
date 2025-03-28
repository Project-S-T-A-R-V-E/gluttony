# import random
# import time

# def getGPS():
#     random.seed(time.time())
#     return [random.randint(0,100), random.randint(0,100)]

# import subprocess

# try:
#     # Run the command with sudo privileges
#     process = subprocess.Popen(
#         ["sudo", "cat", "/dev/ttyAMA0"],
#         stdout=subprocess.PIPE,
#         stderr=subprocess.PIPE,
#         text=True  # Capture output as a string
#     )

#     # Continuously read the output line by line
#     for line in process.stdout:
#         if line.startswith("$GPGGA"):  # Check if the line starts with $GPGGA
#             print(line.strip())  # Print the line
#             break  # Exit the loop after the first match

#     # Wait for the process to complete (optional, if you'd like to clean up)
#     process.terminate()

# except Exception as e:
#     print(f"An error occurred: {e}")

import pynmea2

# Example GPGGA sentence
gpgga_sentence = "$GPGGA,045153.00,3921.15279,N,07632.65870,W,1,10,0.80,97.1,M,-34.6,M,,*5F"

# Parse the sentence
message = pynmea2.parse(gpgga_sentence)

# Extract useful data
print("Timestamp:", message.timestamp)
print("Latitude:", message.latitude)
print("Longitude:", message.longitude)
print("Altitude:", message.altitude)
print("Number of Satellites:", message.num_sats)