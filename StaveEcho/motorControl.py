import time
from adafruit_servokit import ServoKit 

# 0: Base, 1: Ref, 2: Yaw, 3: Pitch, 4: Linact, 8: R-RPWM, 9: R-LPWM, 10: L-RPWM, 11: L-LPWM

# Base Max: 90, Min: 10
# linAct Max: 180, Min:20
# Yaw Max: 179, Min: 0
# Pitch:  


# Servo Motors
def actuation(pitchDeg, yawDeg, armHeight, baseDeg):
    move = ServoKit(channels = 16)
    base = 0
    baseRef = 1
    yaw = 2
    pitch = 3
    linact = 4
    # baseDeg = int(icmbaseDeg) 
    print(baseDeg)
    print(type(baseDeg))
    try:
        move.servo[base].angle = int(baseDeg)
    except ValueError:
        print(f"Error: baseDeg must be an integer, got {baseDeg} of type {type(baseDeg)}")
    # move.servo[baseRef].angle = (-1*baseDeg) +180
    # move.servo[yaw].angle = yawDeg    
    # move.servo[pitch].angle = pitchDeg
    # move.servo[linact].angle = armHeight

 

# Drive Motors
