import random

random.seed(0)

def getPYR():
    return [random.randint(0, 100), random.randint(0, 100), random.randint(0, 100)]

def getAccelXYZ():
    return [random.randint(0, 100), random.randint(0, 100), random.randint(0, 100)]

def getMagXYZ():
    return [random.randint(0, 100), random.randint(0, 100), random.randint(0, 100)]


