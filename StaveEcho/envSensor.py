import random
import time

def getHumidity():
    random.seed(time.time())
    return random.randint(60,70)

def getTemp():
    random.seed(time.time())
    return random.randint(80,99)

def getVoltage():
    random.seed(time.time())
    return random.randint(12,13)

