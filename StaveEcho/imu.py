import random
import time
import icm20948 

def getIMU(): #TODO: Implement actual sensor reading
    # random.seed(time.time())
    # return [random.randint(0, 100), random.randint(0, 100), random.randint(0, 100)]
    try:
        sensor = icm20948.ICM20948()
        pyr = sensor.read_gyro_data()
        accel = sensor.read_accel_data()
        mag = sensor.read_mag_data()
        return pyr
        # return (pyr['x'], pyr['y'], pyr['z'], accel['x'], accel['y'], accel['z'], mag['x'], mag['y'], mag['z'])
    except OSError as e:
        print(f"Error accessing the sensor: {e}")
        return None

while True:
    print(getIMU())
    time.sleep(2)

