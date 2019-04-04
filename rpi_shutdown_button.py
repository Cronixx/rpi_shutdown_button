#!/usr/bin/python
from subprocess import call
from time import sleep
import RPi.GPIO as GPIO

"""
Place shutdown-button.service in /etc/systemd/system,
then active by using systemctl enable shutdown-button.service.

You also need to specify the path of the python script in shutdown-button.service,
for example by using 'readlink -f <filename>'.
Otherwise you can store that path in a variable and call $VARIABLE in shutdown-button.service ExecStart.

"""

# config section
input_pin_number = 18
should_print_to_console = True

# initialization
GPIO.setmode(GPIO.BCM)
GPIO.setup(input_pin_number, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# block until rise in voltage is detected
GPIO.wait_for_edge(input_pin_number, GPIO.RISING)
if should_print_to_console:
    print('Shutdown initiated ...')
call("systemctl poweroff", shell=True)
