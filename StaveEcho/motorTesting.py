import time
from adafruit_pca9685 import PCA9685
from board import SCL, SDA
import busio
# Create the I2C bus interface
i2c_bus = busio.I2C(SCL, SDA)
# Create a simple PCA9685 class instance
pca = PCA9685(i2c_bus)

def set_pwm(channel, frequency, duty_cycle):
    # Set the PWM frequency
    pca.frequency = frequency
    # Calculate the pulse length
    pulse_length = int(duty_cycle * 65535 / 100)
    # Set the PWM signal for the specified channel
    pca.channels[channel].duty_cycle = pulse_length

while True:
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~")
        ch = input("ch: ")  # Input is a string, don't convert it to int immedi>
        if ch == "s":
                set_pwm(8, 50, 0)
                set_pwm(9, 50, 0)
                set_pwm(10, 50, 0)
                set_pwm(11, 50, 0)
                print("STOP")
        elif ch == "f":
                frequency = int(input("Freq: "))
                duty_cycle = int(input("DC%: "))
                set_pwm(8, frequency, duty_cycle)
                set_pwm(9, frequency, duty_cycle)
                print("FORWARD")
        elif ch == "b":
                frequency = int(input("Freq: "))
                duty_cycle = int(input("DC%: "))
                set_pwm(10, frequency, duty_cycle)
                set_pwm(11, frequency, duty_cycle)
                print("BACKWARD")
        elif ch == "l":
                frequency = int(input("Freq: "))
                duty_cycle = int(input("DC%: "))
                set_pwm(9, frequency, duty_cycle)
                set_pwm(11, frequency, duty_cycle)
                print("LEFT TURN")
        elif ch == "r":
                frequency = int(input("Freq: "))
                duty_cycle = int(input("DC%: "))
                set_pwm(10, frequency, duty_cycle)
                set_pwm(8, frequency, duty_cycle)
                print("RIGHT TURN")
        else:
                try:
                        ch = int(ch)
                        frequency = int(input("Freq: "))
                        duty_cycle = int(input("DC%: "))
                        set_pwm(ch, frequency, duty_cycle)
                except ValueError:
                        print("Invalid input. Please try again.")