# microbit-cypher-games
A selection of ideas and files that can be used for wireless encryption / eavesdropping / encryption games with the BBC microbit.

The programs are all written in Python and should be flashed to the microbit using the Mu editor.

The idea is that one group sends messages to each other wirelessly either in plaintext or encoded using a simple Caesar cypher - they can use a web site, Python program, Scratch program or paper cypher wheel to encode their messages. They use cypher-2way-messages.py to send and receive their messages. If you don't have this group in your actvity the teacher can use cypher-tx-2messages.py or cypher-broadcast.py to broadcast messages.

The second group are the eavesdropprs and code-breakers - they use the cypher-receiver.py code to receive messages and show them on the microbit display. They will have to be quick to jot them down and then use another method such as a Python program to decode them.

The next step is to get the microbit to do the brute-force attack on the Caesar cypher - cypher-rx-brute-force.py does this. It is very slow, however, scrolling 26 versions of each message received on the display.

Finally, if you have access to an Adafruit/Pimoroni/Sparkfun thermal printer, you can connect this up to the microbit. The program cypher-brute-force-printer.py will print each attempt on the till-roll printer.
