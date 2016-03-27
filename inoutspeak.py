#! /usr/bin/python

import bluetooth
import time
import os

name1 = "Hello, Hello Bruna"
name2 = "Hello, Hello Button"

def say(name):
    os.system('espeak -ven+f2 -k5 -s150 "{}"'.format(name))

while True:
    print(time.strftime("%a, %d %b %Y %H:%M:%S@", time.gmtime()))
    print("Devices in the room: ")

    result = bluetooth.lookup_name('C4:3A:BE:8E:9E:70', timeout=5)
    if (result != None):
        print("Bruna in")
        say(name1)
    else:
        print("Bruna out")

    result = bluetooth.lookup_name('00:14:01:21:11:18', timeout=5)
    if (result != None):
        print("Button in")
        say(name2)
    else:
        print("Button out")

    time.sleep(60)
