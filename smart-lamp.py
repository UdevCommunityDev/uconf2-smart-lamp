#!/usr/bin/env python
############################################
#        bendahmane.amine@gmail.com        #
############################################

import RPi.GPIO as GPIO
import urllib2
import cPickle
import datetime
import os, time
from sklearn.svm import SVC

# setup
GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)

lamp = 21
GPIO.setup(lamp, GPIO.OUT)

pretrained_model_path = "pretrained-smart-lamp.model"

print "loading pretrained model..."
if os.path.isfile(pretrained_model_path):
    with open(pretrained_model_path, 'rb') as f:
        model = cPickle.load(f)
else:
    print "Error: file '{}' not found".format(pretrained_model_path)
    exit()

print("Starting...")
GPIO.output(lamp, 1)
time.sleep(1.5)
GPIO.output(lamp, 0)
time.sleep(0.2)

print("Listening...")
t = time.time()
while True:
    # get the lamp status from the server
    status = urllib2.urlopen("http://udevcommunity.org/uconf2-iot-test/get_lamp_status.php").read()
    if (status == '1'):
        GPIO.output(lamp, 1)
        now = datetime.datetime.now()
        predicted_delay = model.predict([now.hour])
        print(predicted_delay)
        time.sleep(predicted_delay)
        GPIO.output(lamp, 0)
        status = urllib2.urlopen("http://udevcommunity.org/uconf2-iot-test/change_lamp_status.php")

    elif (status == '0'):
        GPIO.output(lamp, 0)

#GPIO.cleanup()
