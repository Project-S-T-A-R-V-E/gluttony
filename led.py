import time
import board
import neopixel


def power_on():
    pixel_pin = board.D18
    num_pixels = 11
    brightness = .1

    pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=brightness, auto_write=False)

    for i in range(255):
        pixels.fill((i, i, i))
        pixels.show()
        time.sleep(0.01)
    time.sleep(0.5)
    for i in range(255, 0, -1):
        pixels.fill((i, i, i))
        pixels.show()
    pixels.fill((0, 0, 0))
    pixels.show()


def i2c_check(status):
    pixel_pin = board.D18
    num_pixels = 11
    brightness = .1

    pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=brightness, auto_write=False)

    if status == "wait":
        pixels.fill((0, 0, 0))
        pixels[9] = (0, 255, 0)
        pixels[10] = (0, 0, 255)
        pixels[0] = (255, 255, 0)
        pixels.show()
    elif status == "pass":
        pixels.fill((0, 0, 0))
        pixels[9] = (0, 255, 0)
        pixels[10] = (0, 0, 255)
        pixels[0] = (0, 255, 0)
        pixels.show()
    elif status == "fail":
        pixels.fill((0, 0, 0))
        pixels[9] = (0, 255, 0)
        pixels[10] = (0, 0, 255)
        pixels[0] = (255, 0, 0)
        pixels.show()
    else:
        pixels.fill((255, 0, 0))
        pixels.show()


def gps_check(status):
    pixel_pin = board.D18
    num_pixels = 11
    brightness = .1

    pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=brightness, auto_write=False)

    if status == "wait":
        pixels.fill((0, 0, 0))
        pixels[9] = (0, 0, 255)
        pixels[10] = (255, 255, 255)
        pixels[0] = (255, 255, 0)
        pixels.show()
    elif status == "pass":
        pixels.fill((0, 0, 0))
        pixels[9] = (0, 0, 255)
        pixels[10] = (255, 255, 255)
        pixels[0] = (0, 255, 0)
        pixels.show()
    elif status == "fail":
        pixels.fill((0, 0, 0))
        pixels[9] = (0, 0, 255)
        pixels[10] = (255, 255, 255)
        pixels[0] = (255, 0, 0)
        pixels.show()
    else:
        pixels.fill((255, 0, 0))
        pixels.show()


def wifi_check(status):
    pixel_pin = board.D18
    num_pixels = 11
    brightness = .1

    pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=brightness, auto_write=False)

    if status == "wait":
        pixels.fill((0, 0, 0))
        pixels[9] = (0, 255, 255)
        pixels[10] = (0, 255, 255)
        pixels[0] = (255, 255, 0)
        pixels.show()
    elif status == "pass":
        pixels.fill((0, 0, 0))
        pixels[9] = (0, 255, 255)
        pixels[10] = (0, 255, 255)
        pixels[0] = (0, 255, 0)
        pixels.show()
    elif status == "fail":
        pixels.fill((0, 0, 0))
        pixels[9] = (0, 255, 255)
        pixels[10] = (0, 255, 255)
        pixels[0] = (255, 0, 0)
        pixels.show()
    else:
        pixels.fill((255, 0, 0))
        pixels.show()


def py_check(status):
    pixel_pin = board.D18
    num_pixels = 11
    brightness = .1

    pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=brightness, auto_write=False)

    if status == "wait":
        pixels.fill((0, 0, 0))
        pixels[9] = (0, 0, 255)
        pixels[10] = (255, 255, 0)
        pixels[0] = (255, 255, 0)
        pixels.show()
    elif status == "pass":
        pixels.fill((0, 0, 0))
        pixels[9] = (0, 0, 255)
        pixels[10] = (255, 255, 0)
        pixels[0] = (0, 255, 0)
        pixels.show()
    elif status == "fail":
        pixels.fill((0, 0, 0))
        pixels[9] = (0, 0, 255)
        pixels[10] = (255, 255, 0)
        pixels[0] = (255, 0, 0)
        pixels.show()
    else:
        pixels.fill((255, 0, 0))
        pixels.show()


def client_check(status):
    pixel_pin = board.D18
    num_pixels = 11
    brightness = .1

    pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=brightness, auto_write=False)

    if status == "wait":
        pixels.fill((0, 0, 0))
        pixels[9] = (255, 0, 255)
        pixels[10] = (255, 255, 255)
        pixels[0] = (255, 255, 0)
        pixels.show()
    elif status == "pass":
        pixels.fill((0, 0, 0))
        pixels[9] = (255, 0, 255)
        pixels[10] = (255, 255, 255)
        pixels[0] = (0, 255, 0)
        pixels.show()
    elif status == "fail":
        pixels.fill((0, 0, 0))
        pixels[9] = (255, 0, 255)
        pixels[10] = (255, 255, 255)
        pixels[0] = (255, 0, 0)
        pixels.show()
    else:
        pixels.fill((255, 0, 0))
        pixels.show()


def headlights(status):

    pixel_pin = board.D18
    num_pixels = 11
    brightness = 1

    pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=brightness, auto_write=False)

    if status == "OFF":
        pixels.fill((0, 0, 0))
        pixels.show()
    elif status == "ON":
        pixels.fill((255, 255, 255))
        pixels.show()
    else:
        pixels.fill((255, 0, 0))
        pixels.show()


        
print("Testing power_on function...")
power_on()
time.sleep(1)

print("Testing i2c_check function...")
for status in ["wait", "pass", "fail", "unknown"]:
    print(f"  Status: {status}")
    i2c_check(status)
    time.sleep(1)

print("Testing gps_check function...")
for status in ["wait", "pass", "fail", "unknown"]:
    print(f"  Status: {status}")
    gps_check(status)
    time.sleep(1)

print("Testing wifi_check function...")
for status in ["wait", "pass", "fail", "unknown"]:
    print(f"  Status: {status}")
    wifi_check(status)
    time.sleep(1)

print("Testing py_check function...")
for status in ["wait", "pass", "fail", "unknown"]:
    print(f"  Status: {status}")
    py_check(status)
    time.sleep(1)

print("Testing client_check function...")
for status in ["wait", "pass", "fail", "unknown"]:
    print(f"  Status: {status}")
    client_check(status)
    time.sleep(1)

print("Testing headlights function...")
for status in ["OFF", "ON", "unknown"]:
    print(f"  Status: {status}")
    headlights(status)
    time.sleep(1)