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
            if led_state == False:
                #led.value(1)
                #time.sleep(.5)
                while button.value() == 0:
                    led_state = True
                    led_control(led_state)
                    led_state = button_hold(initial_count, led_state)
            elif led_state == True:
                while button.value() == 0:
                    led_state = False
                    led_control(led_state)
                    led_state = button_hold(initial_count, led_state)

            print("wait .1")
            time.sleep(.1)
            print("ready")


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
    if led_state == False:
        led.value(1)  # led_on
        print("LED On")
    elif led_state == True:
        led.value(0)  # led_off
        print("LED OFF")
    return (led_state)


button_input(initial_count, led_state)

