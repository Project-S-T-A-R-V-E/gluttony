import random
import time

def getGPS():
    random.seed(time.time())
    return [random.randint(0,100), random.randint(0,100)]
