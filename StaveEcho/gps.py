import subprocess
import pynmea2

def getGPS(): # returns lat,lon

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
                msg = pynmea2.parse(line.strip())  # Parse the NMEA sentence
                print(float(msg.latitude), float(msg.longitude))
                return float(msg.latitude), float(msg.longitude)  # Return latitude and longitude
                break  # Exit the loop after the first match

        # Wait for the process to complete (optional, if you'd like to clean up)
        process.terminate()

    except Exception as e:
        print(f"An error occurred: {e}")

