from machine import Pin
from utime import sleep_ms


button = Pin(0, Pin.IN, Pin.PULL_UP)   #Internal pull-up
led = Pin(1, Pin.OUT)
led_state=False                                #0 means that the light is currently off

while True:
    #print(button.value())
    if button.value() == 0:       #key press
        if led_state == False:
            led.value(1)
            sleep_ms = 100
            while button.value() == 0:
                led_state = True
            print("LED ON")
        else:
            led.value(0)
            sleep_ms=100
            while button.value() == 0:
                led_state = False
            print("LED OFF")


