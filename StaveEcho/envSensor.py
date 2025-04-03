import random
import time

def getHumidity(): #TODO: Implement actual sensor reading
    random.seed(time.time())
    return random.randint(60,70)

def getTemp(): #TODO: Implement actual sensor reading
    random.seed(time.time())
    return random.randint(80,99)

def getVoltage(): #TODO: Implement actual sensor reading
    random.seed(time.time())
    return random.randint(12,13)

