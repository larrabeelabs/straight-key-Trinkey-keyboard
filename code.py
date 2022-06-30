# A simple neat keyboard demo in CircuitPython

import time
import board
import touchio
import digitalio
import neopixel
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

touch = touchio.TouchIn(board.TOUCH)
switch = digitalio.DigitalInOut(board.SWITCH)
switch.switch_to_input(pull=digitalio.Pull.UP)


keypress_pins = [touch, switch]
# Our array of key objects
key_pin_array = []
# The Keycode sent for each button, will be paired with a control key
keys_pressed = [Keycode.LEFT_CONTROL]
control_key = False

# The keyboard object!
time.sleep(1)  # Sleep for a bit to avoid a race condition on some systems
keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)  # We're in the US :)

pixels = neopixel.NeoPixel(board.NEOPIXEL, 1)

while True:
    # Check each pin
    if touch.value or not switch.value:
        i=0
        print("Pad touched!")
        pixels.fill((75,20,30))
        key=keys_pressed[i]
        keyboard.press(key)
        time.sleep(0.03)
        pixels.fill((0,0,0))
    else:
        keyboard.release_all()
