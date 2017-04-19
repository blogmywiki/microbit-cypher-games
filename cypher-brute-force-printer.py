# This program waits for a radio message to be received then
# does a brute-force attack assuming message is a Ceasar cypher
# and prints each attempt on an Adafruit/Pimoroni/Sparkfun type
# thermal printer - connect pin 8 on microbit to yellow TTL wire
# on printer, connect GND/0v on microbit to black printer wire.

import radio, microbit
from microbit import display, sleep

radio.on()
alphabet = "abcdefghijklmnopqrstuvwxyz"
incoming = ""

microbit.uart.init(baudrate=19200, bits=8, parity=None, stop=1, tx=microbit.pin8, rx=None)

while not incoming:
    incoming = radio.receive()
    if incoming:
        for key in range(26):
            guess = ""
            for letter in incoming:
                if letter in alphabet:
                    position = alphabet.find(letter)
                    newPosition = (position - key) % 26
                    guess = guess + alphabet[newPosition]
                else:
                    guess = guess + letter
            # display.scroll(str(key)+guess)
            microbit.uart.write(str(key)+guess+"\n")
            sleep(1000)
