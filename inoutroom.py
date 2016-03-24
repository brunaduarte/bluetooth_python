#! /usr/bin/python

import bluetooth
import time

while True:
    print time.strftime("%a, %d %b %Y %H:%M:%S@", time.gmtime())
    print "Devices in the room: "
    
    result = bluetooth.lookup_name('C4:3A:BE:8E:9E:70', timeout=5)
    
    if (result != None):
        print "Bruna in"
    else:
        print "Bruna out"
        
    result = bluetooth.lookup_name('00:14:01:21:11:18', timeout=5)
    
    if (result != None):
        print "Button in"
    else:
        print "Button out"
        
    time.sleep (60)
        
