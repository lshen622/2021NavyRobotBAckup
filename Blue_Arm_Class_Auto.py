import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
import xarm


class Arm_Class():
    def __init__(self,servo_id,init_angle=90):

        self.servo_id = servo_id
        self.init_angle = init_angle
        servo_object = xarm.Servo(self.servo_id, self.init_angle)

#         angle range -125 to 125

#         arm = xarm.Controller('USB')
#         arm = xarm.Controller('USB') !!!!!!!

    def moveto(self,angle):

        arm.setPosition(self.servo_id, angle, wait=True)
#         angle must be input as float aka 90.0

    def main():



if __name__ == '__main__':
    arm = xarm.Controller('USB')
    while True:
        main()
