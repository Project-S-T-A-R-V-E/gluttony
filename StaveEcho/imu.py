import random
import time
import icm20948 

def getimu(): #TODO: Implement actual sensor reading
    # random.seed(time.time())
    # return [random.randint(0, 100), random.randint(0, 100), random.randint(0, 100)]
    sensor = icm20948.ICM20948()
    pyr = sensor.read_gyro_data()
    accel = sensor.read_accel_data()
    mag = sensor.read_mag_data()
    return (pyr['x'], pyr['y'], pyr['z'], accel['x'], accel['y'], accel['z'], mag['x'], mag['y'], mag['z'])

while True:
    print(getimu())
    time.sleep(2)

