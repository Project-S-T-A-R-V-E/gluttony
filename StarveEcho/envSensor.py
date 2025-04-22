# import random
# import time
# import Adafruit_DHT

# # Sensor type and GPIO pin
# EXT_DHT_SENSOR = Adafruit_DHT.DHT22
# EXT_DHT_PIN = 4  # Replace with the GPIO pin number where the DATA pin is connected

# def getInternalHumidity():
#     # Replace with actual internal sensor logic if available
#     return None

# def getInternalTemp():
#     # Replace with actual internal sensor logic if available
#     return None

# def getExternalHumidity():
#     humidity, _ = Adafruit_DHT.read(EXT_DHT_SENSOR, EXT_DHT_PIN)
#     if humidity is not None:
#         return round(humidity, 2)
#     else:
#         print("Failed to retrieve humidity data from DHT22 sensor")
#         return None

# def getExternalTemp():
#     _, temperature = Adafruit_DHT.read(EXT_DHT_SENSOR, EXT_DHT_PIN)
#     if temperature is not None:
#         return round(temperature, 2)
#     else:
#         print("Failed to retrieve temperature data from DHT22 sensor")
#         return None

# def getVoltage():
#     # Placeholder for voltage reading logic
#     return None



# print(getExternalHumidity())
# print(getInternalHumidity())

import time
import adafruit_dht
import board

dht_device = adafruit_dht.DHT22(board.D4)

while True:
    try:
        temperature_c = dht_device.temperature
        temperature_f = temperature_c * (9 / 5) + 32

        humidity = dht_device.humidity

        print("Temp:{:.1f} C / {:.1f} F    Humidity: {}%".format(temperature_c, temperature_f, humidity))
    except RuntimeError as err:
        print(err.args[0])

    time.sleep(2.0)