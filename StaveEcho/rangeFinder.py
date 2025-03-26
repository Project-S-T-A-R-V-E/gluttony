import random
import time

def getRangeFinder():
    # Get the range finder value
    random.seed(time.time())
    return (random.randint(0, 8))