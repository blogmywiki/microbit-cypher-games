# This program displays any incoming radio messages
# as received on the microbit.

import radio
from microbit import display, sleep

radio.on()

while True:
    incoming = radio.receive()
    if incoming:
        display.scroll(incoming)
        sleep(4000)
        