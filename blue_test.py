import xarm
from time import sleep

arm = xarm.Controller('USB')

servo3 = xarm.Servo(1, 90.0)

arm.setPosition(1, 0.0, 100, wait=True)
arm.setPosition(2, 0.0, 100, wait=True)
arm.setPosition(3, 0.0, 100, wait=True)
arm.setPosition(4, 0.0, 100, wait=True)
arm.setPosition(5, 0.0, 100, wait=True)
arm.setPosition(6, 0.0, 100, wait=True)