#!/usr/bin/env python
############################################
#        bendahmane.amine@gmail.com        #
############################################

import RPi.GPIO as GPIO
import urllib2
import time

# setup
GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)
#GPIO.setmode(GPIO.BCM)
#GPIO.setwarning(False)

lamp = 29
GPIO.setup(lamp, GPIO.OUT)

# test led
print("Starting...")
GPIO.output(lamp, 1)
time.sleep(1.5)
GPIO.output(lamp, 0)
time.sleep(0.2)

# listen to server 
print("Listening...")
t = time.time()
while True:
    # get the lamp status from the server
    status = urllib2.urlopen("http://udevcommunity.org/uconf2-iot-test/get_lamp_status.php").read()
    if (status == '1')
        GPIO.output(lamp, 1):
    elif (status == '0')
        GPIO.output(lamp, 0):

#GPIO.cleanup()
