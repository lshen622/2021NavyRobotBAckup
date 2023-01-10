import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

class Arm_Class_Auto():
    def __init__(self,pin,minduty,maxduty):
        self.pin = pin
        pulse_in_Hz = 50
        GPIO.setup(self.pin,GPIO.OUT)
        self.servo = GPIO.PWM(self.pin,pulse_in_Hz) # Note: 50 = 50Hz pulse
        self.servo.start(0)
        self.minduty = minduty
        self.maxduty = maxduty

    def moveto(self,angle):

        if angle < self.minduty:
            angle = self.minduty
        if angle > self.maxduty:
            angle = self.maxduty

        if angle >= self.minduty and angle <= self.maxduty:
            self.servo.ChangeDutyCycle(angle)
        else:
            raise ValueError("Duty Cycle Must be Within Range 2.5 to 12.5")
        return angle

    def stop(self):
        self.servo1.ChangeDutyCycle(0);
        sleep(0.1)