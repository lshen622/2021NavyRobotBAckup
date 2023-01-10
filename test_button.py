import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
channel = 26
GPIO.setup(channel, GPIO.IN, pull_up_down=GPIO.PUD_UP)




GPIO.add_event_detect(channel, GPIO.RISING)
<Code to execute normally in the user-program>
if GPIO.event_detected(channel):
    <Code to execute after detection of edge at GPIO>


    GPIO.add_event_detect(26, GPIO.FALLING, callback=myInterrupt, bouncetime=500)