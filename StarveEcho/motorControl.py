import time
from adafruit_servokit import ServoKit 
import time
from adafruit_pca9685 import PCA9685
from board import SCL, SDA
import busio

# 0: Base, 1: Ref, 2: Yaw, 3: Pitch, 4: Linact, 8: R-RPWM, 9: R-LPWM, 10: L-RPWM, 11: L-LPWM

# Base Max: 90, Min: 10
# linAct Max: 180, Min:20
# Yaw Max: 179, Min: 0
# Pitch:  

# Drive Motors Assuming Left Side spinning clockwise is forward
def drive(L,R):
    # Initialize I2C bus and PCA9685
    i2c_bus = busio.I2C(SCL, SDA)
    pwm = PCA9685(i2c_bus)
    pwm.frequency = 50  # Set frequency to 50Hz

    # Define PWM channels for BTS7960
    lBKW = 12
    lFWD = 13
    rFWD = 14
    rBKW = 15
    
    # ++: Both motors forward
    if L > 0 and R > 0:
        pwm.channels[lFWD].duty_cycle = int(abs(L) * 65535 / 100)
        pwm.channels[lBKW].duty_cycle = 0
        pwm.channels[rFWD].duty_cycle = int(abs(R) * 65535 / 100)
        pwm.channels[rBKW].duty_cycle = 0
        # print("Forward! " + str(L) + " " + str(R))
    
    # +-: Left motor forward, Right motor backward
    elif L > 0 and R < 0:
        pwm.channels[lFWD].duty_cycle = int(abs(L) * 65535 / 100)
        pwm.channels[lBKW].duty_cycle = 0
        pwm.channels[rFWD].duty_cycle = 0
        pwm.channels[rBKW].duty_cycle = int(abs(R) * 65535 / 100)
        # print("Turn Right! " + str(L) + " " + str(R))
    
    # -+: Left motor backward, Right motor forward
    elif L < 0 and R > 0:
        pwm.channels[lFWD].duty_cycle = 0
        pwm.channels[lBKW].duty_cycle = int(abs(L) * 65535 / 100)
        pwm.channels[rFWD].duty_cycle = int(abs(R) * 65535 / 100)
        pwm.channels[rBKW].duty_cycle = 0
        # print("Turn Left! " + str(L) + " " + str(R))

    # --: Both motors backward
    elif L < 0 and R < 0:
        pwm.channels[lFWD].duty_cycle = 0
        pwm.channels[lBKW].duty_cycle = int(abs(L) * 65535 / 100)
        pwm.channels[rFWD].duty_cycle = 0
        pwm.channels[rBKW].duty_cycle = int(abs(R) * 65535 / 100)
        # print("Backwards! " + str(L) + " " + str(R))
    # 00: Stop both motors
    else:
        pwm.channels[lBKW].duty_cycle = 0
        pwm.channels[lFWD].duty_cycle = 0
        pwm.channels[rFWD].duty_cycle = 0
        pwm.channels[rBKW].duty_cycle = 0
        # print("STOP! " + str(L) + " " + str(R))


# Servo Motors
def actuation(pitchDeg, yawDeg, armHeight, baseDeg):
    move = ServoKit(channels = 16)
    base = 0
    baseRef = 1
    yaw = 2
    pitch = 3
    linact = 4

    move.servo[base].angle = int(baseDeg)
    move.servo[baseRef].angle = (-1*baseDeg) +180
    move.servo[yaw].angle = yawDeg    
    move.servo[pitch].angle = pitchDeg
    move.servo[linact].angle = armHeight