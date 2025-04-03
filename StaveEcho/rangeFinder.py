import random
import time

def getRangeFinder(): #TODO: Implement actual sensor reading
    # Get the range finder value
    random.seed(time.time())
    return (random.randint(0, 8))