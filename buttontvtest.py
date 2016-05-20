#! /usr/bin/python

import os
import time
import serial

count = 0 

bluetoothSerial = serial.Serial("/dev/rfcomm0", baudrate=9600)

while 1:

        #print bluetoothSerial.readline()
        n = bluetoothSerial.readline()
        
        if(n != 0):
            
            count = count +1
            
            if(count%3==0):
                os.system("irsend SEND_ONCE Philips 1")
                os.system("irsend SEND_ONCE Philips 2")
            if(count%3==1):
                os.system("irsend SEND_ONCE Philips 2")
                os.system("irsend SEND_ONCE Philips 3")
            if(count%3==2):
                os.system("irsend SEND_ONCE Philips 3")
                os.system("irsend SEND_ONCE Philips 4")
                        
        else:
         # No data is ready to be processed
         time.sleep(0.5)