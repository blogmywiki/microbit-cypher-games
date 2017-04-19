import radio
from microbit import sleep, display

message = "tb pxfi xq axtk"

radio.on()

while True:
    display.show('TX',wait=False)
    radio.send(message)
    sleep(4000)
    