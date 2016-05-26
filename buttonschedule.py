#! /usr/bin/python
from urllib2 import urlopen
import urllib2
import urllib
import json
import datetime
import requests
import os
import time
import serial
import bluetooth

count = 0 
restart = 0 

startTime = time.time()

name1 = "Hello, Hello Bruna"
name2 = "Hello, Hello Button"

bluetoothSerial = serial.Serial("/dev/rfcomm0", baudrate=9600) 

timestr = time.strftime("%a, %d %b %Y %H:%M:%S", time.gmtime())

def say(name):
    os.system('espeak -ven+f2 -k5 -s150 "{}"'.format(name))
 
def bluetoothInOut():
    
    bluetoothSerial = serial.Serial("/dev/rfcomm0", baudrate=9600) 
    
    restart = 0 
  
    print(timestr)
    print("Devices in the room: ") 
    result1 = bluetooth.lookup_name('C4:3A:BE:8E:9E:70', timeout=5)
    if(result1 != None):
        print("Bruna in")
        say(name1)
        restart=0
             
    else:
        print("Bruna out")
        restart = restart + 1
                
    result2 = bluetooth.lookup_name('00:14:01:21:11:18', timeout=10)
    
    if(result2 != None):
        print("Button in")
        say(name2)
        #serial.open()
        restart=0
        
                
    else:
        print("Button out")
        restart = restart + 1
                
    print (time.time())
    print (time.clock())
    
    return restart

def getSchedule():
#Gets information about the current program in that specific channel
    
    url = 'http://api.rovicorp.com/TVlistings/v9/listings/linearschedule/891474/info?locale=en-IE&duration=60&inprogress=true&oneairingpersourceid=false&sourceid=26082&format=json&apikey=wywp4j4hpy37btp4bnaceb7y'

    response1 = urllib2.urlopen(url)

    content1 = response1.read()

    data1 = json.loads(content1.decode("utf8"))

    print ("Title:", data1['LinearScheduleResult']['Schedule']['Airings'][0]['Title'])
    print ("Genre:", data1['LinearScheduleResult']['Schedule']['Airings'][0]['Subcategory'])
    print ("Synopsis:", data1['LinearScheduleResult']['Schedule']['Airings'][0]['Copy'])
    print ("ProgramId:", data1['LinearScheduleResult']['Schedule']['Airings'][0]['ProgramId'])

def getAirings():
#Gets the next airing for the program at that time

    url1 = 'http://api.rovicorp.com/TVlistings/v9/listings/programdetails/891474/'
    url2 = '/info?locale=en-IE&copytextformat=PlainText&include=Program%2C+Seasons&imagecount=5&duration=20160&inprogress=false&sourceid=26082&pagesize=0&format=json&apikey=wywp4j4hpy37btp4bnaceb7y'

    #id = data1['LinearScheduleResult']['Schedule']['Airings'][0]['ProgramId']
    id = '3994568'
    url3 = url1+id+url2
    #print (url3)

    response2 =  urllib2.urlopen(url3)

    content2 = response2.read()

    data2 = json.loads(content2)

    print ("Next Streaming:", data2['ProgramDetailsResult']['Schedule']['Airings'][0]['AiringTime'])    
    
file = open('AccessUser.txt', 'w') #Overwrites what was in the file
file.write(timestr)
file.write("\n")
file.close()
#time.sleep(1)    

restart = bluetoothInOut()

while 1:
    
    if(restart == 2):
        #time.sleep(3)
       
        restart = bluetoothInOut()
        bluetoothSerial = serial.Serial("/dev/rfcomm0", baudrate=9600)
        time.sleep(0.5) #minimun time I could get
    
    else:
        
        #if(bluetoothSerial.available()):
        #time.sleep(5)        
        #y = bluetoothSerial.inWaiting() 
        n = bluetoothSerial.readline() 
     
        if(n != 0):
            timeAccess = time.strftime("%H:%M:%S", time.gmtime())        
            count = count +1
                                   
            if(count%3==1):
                getSchedule()          
                os.system("irsend SEND_ONCE Philips 1")
                os.system("irsend SEND_ONCE Philips 1")
                os.system("irsend SEND_ONCE Philips 2")
            
                file = open('AccessUser.txt', 'a')
                file.write("Channel1: ")
                file.write(timeAccess)
                file.write(" \n")
                file.close()
            
                print("Time: ")
                print(time.strftime("%H:%M:%S", time.gmtime()))
                
                
            if(count%3==2):
            
                getAirings()
                
                os.system("irsend SEND_ONCE Philips 2")
                os.system("irsend SEND_ONCE Philips 3")
            
                file = open('AccessUser.txt', 'a')
                file.write("Channel2: ")
                file.write(timeAccess)
                file.write(" \n")
                file.close()
                       
                print("Time: ")
                print(time.strftime("%H:%M:%S", time.gmtime()))
				
            if(count%3==0):
                os.system("irsend SEND_ONCE Philips 3")
                os.system("irsend SEND_ONCE Philips 4")
            
                file = open('AccessUser.txt', 'a')
                file.write("Channel3: ")
                file.write(timeAccess)
                file.write(" \n")
                file.close()
                        
                print("Time: ")
                print(time.strftime("%H:%M:%S", time.gmtime()))
                        
        else:
            # No data is ready to be processed
            time.sleep(0.5)
                

            
            
