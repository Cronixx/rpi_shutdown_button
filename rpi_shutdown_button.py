#!/usr/bin/python
from subprocess import call
from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    input_state = GPIO.input(18)
    if not input_state:
        print('Shutdown initiated ...')
        call("systemctl poweroff", shell=True)
    sleep(1)
