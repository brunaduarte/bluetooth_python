from urllib2 import urlopen
import urllib2
import urllib
import json
import datetime
import requests

#Not needing to access the file by now
#file = open ('AccessUser.txt', 'r')
#print file.readlines()
#file.close()

###################################################################################################
#Gets information about the current program in that specific channel
url = 'http://api.rovicorp.com/TVlistings/v9/listings/linearschedule/891474/info?locale=en-IE&duration=60&inprogress=true&oneairingpersourceid=false&sourceid=26082&format=json&apikey=wywp4j4hpy37btp4bnaceb7y'

response1 = urllib2.urlopen(url)

content1 = response1.read()

data1 = json.loads(content1.decode("utf8"))
#L = len(data1)
print ("Title:", data1['LinearScheduleResult']['Schedule']['Airings'][0]['Title'])
print ("Genre:", data1['LinearScheduleResult']['Schedule']['Airings'][0]['Subcategory'])
print ("Synopsis:", data1['LinearScheduleResult']['Schedule']['Airings'][0]['Copy'])
print ("ProgramId:", data1['LinearScheduleResult']['Schedule']['Airings'][0]['ProgramId'])
######################################################################################################
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
#print(data)

