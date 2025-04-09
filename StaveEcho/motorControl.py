import time
from adafruit_servokit import ServoKit 

# 0: Base, 1: Ref, 2: Yaw, 3: Pitch, 4: Linact, 8: R-RPWM, 9: R-LPWM, 10: L-RPWM, 11: L-LPWM

# Base Max: 90, Min: 10
# linAct Max: 180, Min:20
# Yaw Max: 179, Min: 0
# Pitch:  


# Servo Motors
def actuation(L, R, baseDeg, yawDeg, pitchDeg, armLength):
    move = ServoKit(channels = 16)
    base = 0
    baseRef = 1
    yaw = 2
    pitch = 3
    linact = 4
    move.servo[base].angle = 10
    move.servo[baseRef].angle = 170
    move.servo[yaw].angle = 90    
    move.servo[pitch].angle = 80
    move.servo[linact].angle = 20

 

# Drive Motors
