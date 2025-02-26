from time import sleep
from machine import Pin

# Setup pin 2 as an output pin
led = Pin(2, Pin.OUT)

while True:
    led.on()  # Turn the LED on
    print("LED is ON")
    sleep(1)  # Wait for 1 second
    led.off()  # Turn the LED off
    print("LED is OFF")
    sleep(1)  # Wait for 1 second