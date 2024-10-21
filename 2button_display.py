from machine import Pin, I2C
# from setuptools.msvc import PlatformInfo
from ssd1306 import SSD1306_I2C
import time

count = 0
plus_button = Pin(2, Pin.IN, Pin.PULL_UP) # needs a pin assignment (use the gpio pin numbers)
minus_button = Pin(3, Pin.IN, Pin.PULL_UP)
display_update_value = None
button_press = False

def display(display_text):
    i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
    oled = SSD1306_I2C(128, 64, i2c)
    display_text = str(display_text)
    oled.text(display_text, 0, 0)
    oled.show()

def plus_button_input(count):
    if plus_button.value() == 0:
        count += 1
        print(count)
    return count

def minus_button_input(count):
    if minus_button.value() == 0:
        count -= 1
        print(count)
    return count

def display_update(count, display_update_value):
    if count != display_update_value:
        display(count)
        display_update_value = count
    return display_update_value

def debouncer(wait_time):
    time.sleep(wait_time)

display_update_value = display_update(count, display_update_value) # to initialize the screen
while True:
    if minus_button.value() == 0 or plus_button.value() == 0:
        count = plus_button_input(count)
        count = minus_button_input(count)
        display_update_value = display_update(count, display_update_value)
        print(count)
        if button_press == False:
            debouncer(0.3)
        elif button_press == True:
            debouncer(0.2)
        button_press = True
    else:
        button_press = False

