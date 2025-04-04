import subprocess
import pynmea2

def getGPS():

    try:
        # Run the command with sudo privileges
        process = subprocess.Popen(
            ["sudo", "cat", "/dev/ttyAMA0"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True  # Capture output as a string
        )

        # Continuously read the output line by line
        for line in process.stdout:
            if line.startswith("$GPGGA"):  # Check if the line starts with $GPGGA
                # Parse the NMEA sentence
                msg = pynmea2.parse(line)
                latitude = msg.latitude
                longitude = msg.longitude
                # print(f"Latitude: {latitude}, Longitude: {longitude}")
                return [latitude, longitude]
                break  # Exit the loop after the first match

        # Wait for the process to complete (optional, if you'd like to clean up)
        process.terminate()

    except Exception as e:
        print(f"An error occurred: {e}")

# result = getGPS()
# if result:
#     print(result[0])
# else:
#     print("No GPS data available.")
