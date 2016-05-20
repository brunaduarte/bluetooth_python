import os
import time

while 1:
    os.system("irsend SEND_ONCE Philips 1")
    os.system("irsend SEND_ONCE Philips 2")
    time.sleep(0.0095)
    os.system("irsend SEND_ONCE Philips 2")
    os.system("irsend SEND_ONCE Philips 3")
    time.sleep(0.0095)