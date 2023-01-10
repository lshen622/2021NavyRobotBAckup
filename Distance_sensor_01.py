# Fixed distance sensor code
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

class distance_sensor():
    def __init__(self,GPIO_TRIGGER,GPIO_ECHO):
        # Set GPIO Pins
        self.GPIO_TRIGGER = GPIO_TRIGGER
        self.GPIO_ECHO = GPIO_ECHO
        # Set GPIO direction (IN / OUT)
        GPIO.setup(self.GPIO_TRIGGER, GPIO.OUT)
        GPIO.setup(self.GPIO_ECHO, GPIO.IN)
        self.maxTime = 0.04

    def dist(self):
        # Allow sensor to settle
        GPIO.output(self.GPIO_TRIGGER, False)
        time.sleep(.01)
        # set Trigger to HIGH
        GPIO.output(self.GPIO_TRIGGER, True)
        # set Trigger after 0.01ms to LOW
        time.sleep(0.00001)
        GPIO.output(self.GPIO_TRIGGER, False)

        StartTime = time.time()
        timeout = StartTime + self.maxTime
        # Check for rising edge
        while GPIO.input(self.GPIO_ECHO) == 0 and StartTime < timeout:
            StartTime = time.time()

        StopTime = time.time()
        timeout = StopTime + self.maxTime
        # Check for falling edge
        while GPIO.input(self.GPIO_ECHO) == 1 and StopTime < timeout:
            StopTime = time.time()

        # time difference between start and arrival
        TimeElapsed = StopTime - StartTime
        # multiply with the sonic speed (34300 cm/s)
        # and divide by 2, because there and back
        distance = (TimeElapsed * 34300) / 2 # in centimeters
       #  distance = round(distance,3)

        if(distance < 2): # Less than 2cm, set it to 2cm
            distance = 2
        elif(distance > 400): # More than 400 cm, set it to 400cm
            distance = 400

        return distance

sensor = distance_sensor(21,20)
def main():
    while True:
        dist = sensor.dist()
        print(dist)

if __name__ == '__main__':
    try:
        while True:
            main()

    except KeyboardInterrupt:
        print('Execution Aborted By User')
        GPIO.cleanup()