from machine import Pin, I2C
# from setuptools.msvc import PlatformInfo
from ssd1306 import SSD1306_I2C
import time
import os

# count = 0
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
    count += 1
    print(count)
    return count

def minus_button_input(count):
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
def file_reader_or_creator(file):
    print(file)
    print(type(file))
    if file in os.listdir():
        print("file was there")
        # file exists so can read
        with open (file, "r") as file:
            # files are stored as strings, convert to int
            count = int(file.read())
        return count
    else:
        # file does not exist
        count = 0
        return count


count_storate_file = "count_storage.txt"
count = file_reader_or_creator(count_storate_file)
display_update_value = display_update(count, display_update_value) # to initialize the screen
while True:
    if plus_button.value() == 0:
        count = plus_button_input(count)
        button_press = True
        if button_press == False:
            debouncer(0.3)
        elif button_press == True:
            debouncer(0.2)
    elif minus_button.value() == 0:
        count = minus_button_input(count)
        button_press = True
        if button_press == False:
            debouncer(0.3)
        elif button_press == True:
            debouncer(0.2)
    else:
        button_press = False
    display_update_value = display_update(count, display_update_value)
    #print(count)
    with open(count_storate_file, "w") as file:
        # .write only accepts bytes or str
        file.write(str(count))