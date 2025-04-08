import subprocess
import pynmea2

def getGPS():

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
    #             return line.strip()  # Print the line
    #             break  # Exit the loop after the first match

    #     # Wait for the process to complete (optional, if you'd like to clean up)
    #     process.terminate()

    # except Exception as e:
    #     print(f"An error occurred: {e}")

    return [0,1]
