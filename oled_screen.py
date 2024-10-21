from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import time

count = 0

def display(display_text):
    i2c=I2C(0,sda=Pin(0), scl=Pin(1), freq=400000)
    oled = SSD1306_I2C(128, 64, i2c)
    display_text = str(display_text)
    oled.text(display_text, 0, 0)
    oled.show()

#def count(initial):
#    count = initial +1
#    print(count)
#    return count
    

for count in range(100):
    display(count)
    print(count)
    time.sleep(1)