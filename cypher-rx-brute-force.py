# This program waits for a radio message to be received then
# does a brute-force attack assuming message is a Ceasar cypher
# and scrolls each assumed key and attempt on microbit display.

import radio
from microbit import display, sleep

radio.on()
alphabet = "abcdefghijklmnopqrstuvwxyz"

while True:
    # Read any incoming messages.
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
            display.scroll(str(key)+guess)
            sleep(1000)
        
        