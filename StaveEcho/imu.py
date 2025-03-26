import random
import time

def getPYR():
    random.seed(time.time())
    return [random.randint(0, 100), random.randint(0, 100), random.randint(0, 100)]

def getAccelXYZ():
    random.seed(time.time())
    return [random.randint(0, 100), random.randint(0, 100), random.randint(0, 100)]

def getMagXYZ():
    random.seed(time.time())
    return [random.randint(0, 100), random.randint(0, 100), random.randint(0, 100)]


