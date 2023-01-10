from time import sleep
from os import environ
import pygame
import RPi.GPIO as GPIO

# blue arm
import xarm

import Pixy2

# In Pi Terminal
###########################

#sudo apt-get -y install jd
#Install Ds4:
#sudo pip3 install ds4drv
#sudo wget https://raw.githubusercontent.com//chrippa/ds4drv/master/udev/50-ds4drv.rules -O /etc/udev/rules.d/50-ds4drv.rules
#sudo udevadm control --reload-rules
#sudo udevadm trigger
#sudo nano /etc/rc.local
# add next line after # By default this script does nothing
#/usr/local/bin/ds4drv &
# control o control x
# then connect via bluetooth