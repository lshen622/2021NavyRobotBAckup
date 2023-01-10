import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
import numpy as np
from time import sleep

pin = 13
freq = 50
GPIO.setup(pin, GPIO.OUT)
p = GPIO.PWM(pin, freq)
p.start(0)
for duty in np.linspace(2.5,12.5,101):
    p.ChangeDutyCycle(duty)
    print(duty)
    sleep(.1)
    p.ChangeDutyCycle(0)
    sleep(0.5)




p.stop()
GPIO.cleanup()