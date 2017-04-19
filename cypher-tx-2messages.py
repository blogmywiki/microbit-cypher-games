# This program broadcasts 1 of 2 different messages when 
# button A or button B is pressed.

import radio
from microbit import sleep, display

radio.on()

while True:
    if button_a.was_pressed():
        display.show('A')
        radio.send('My secret message 1')
    if button_b.was_pressed():
        display.show('B')
        radio.send('My secret message 2')
    sleep(1000)
    display.clear()
    