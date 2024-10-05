# Goal: Blink the led for each count. Prevent entry when blinking (probably already going to happen)

from machine import Pin
import time

button = Pin(0, Pin.IN, Pin.PULL_UP)  # Internal pull-up
led = Pin(1, Pin.OUT)
led_state = False  # 0 means that the light is currently off
led.value(0)
initial_count = 0


def button_input(initial_count, led_state):
    count = int(initial_count)
    while True:
        if button.value() == 0:  # key press
            if led_state == False: # Triggers if the led is off
                while button.value() == 0:
                    led_state = True
                    led_control(led_state)
                    led_state = button_hold(initial_count, led_state)
            elif led_state == True: # Triggers if the LED is on
                while button.value() == 0:
                    led_state = False
                    led_control(led_state)
                    led_state = button_hold(initial_count, led_state)

            print("wait .1")
            time.sleep(.1)
            print("ready")

def button_input_counter(initial_count):
    count = int(initial_count)
    while True:
        if button.value() == 0:
            count += 1
            print("count value:", count)
            print("activating led_flasher with:", count)
            led_flasher(count)
            print("ready for button press")

def led_flasher(target_count):
    if target_count != 0:
        flash_count = 1
        while target_count != flash_count:
            print("Target Count:", target_count)
            led_control(True)
            flash_count += 1
            print("Flash Count:", flash_count)
            time.sleep(1)
            led_control(False)
            time.sleep(1)
    print("exiting led_flasher")


def button_hold(initial_count, led_state):
    print("Button Hold checker")
    print("Sleep 1")
    time.sleep(.3)

    if button.value() == 0:  # key press
        print("Button Holder Activating!")
        if led_state == False:
            #led.value(1)

            #while button.value() == 0:
            led_state = True
            led_control(led_state)
            time.sleep(1)
        elif led_state == True:
            #while button.value() == 0:

            led_state = False
            led_control(led_state)
            time.sleep(1)
    print("exiting button holder checker")
    return led_state

def led_control(led_state):
    if led_state == True:
        led.value(1)  # led_on
        print("LED On")
    elif led_state == False:
        led.value(0)  # led_off
        print("LED OFF")
    return (led_state)


#button_input(initial_count, led_state)
button_input_counter(initial_count)