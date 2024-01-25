#!/usr/bin/python

from PCA9685 import PCA9685
import time

Dir = [
    'forward',
    'backward',
]
pwm = PCA9685(0x40, debug=False)
pwm.setPWMFreq(50)

class MotorDriver():
    def __init__(self):
        self.PWMA = 0
        self.AIN1 = 1
        self.AIN2 = 2
        self.PWMB = 5
        self.BIN1 = 3
        self.BIN2 = 4

    def MotorRun(self, motor, index, speed):
        if speed > 100:
            return
        if(motor == 0):
            pwm.setDutycycle(self.PWMA, speed)
            if(index == Dir[0]):
                print ("1")
                pwm.setLevel(self.AIN1, 0)
                pwm.setLevel(self.AIN2, 1)
            else:
                print ("2")
                pwm.setLevel(self.AIN1, 1)
                pwm.setLevel(self.AIN2, 0)
        else:
            pwm.setDutycycle(self.PWMB, speed)
            if(index == Dir[0]):
                print ("3")
                pwm.setLevel(self.BIN1, 0)
                pwm.setLevel(self.BIN2, 1)
            else:
                print ("4")
                pwm.setLevel(self.BIN1, 1)
                pwm.setLevel(self.BIN2, 0)

    def MotorStop(self, motor):
        if (motor == 0):
            pwm.setDutycycle(self.PWMA, 0)
        else:
            pwm.setDutycycle(self.PWMB, 0)


class MotionController():
    def __init__(self,motorDriver):
        self.motor = motorDriver
        self.left_motor = 1
        self.right_motor = 0
        self.left_motor_forward = 'backward'
        self.right_motor_forward = 'forward'  #the dc motor is mounted mirrored
        self.left_motor_backward = 'forward'
        self.right_motor_backward= 'backward'  #the dc motor is mounted mirrored

    def forward(self, speed=100,timeout=2):
        self.motor.MotorRun(self.left_motor, self.left_motor_forward , speed)
        self.motor.MotorRun(self.right_motor, self.right_motor_forward , speed)
        time.sleep(timeout)

    def backward(self, speed=100,timeout=2):
        self.motor.MotorRun(self.left_motor, self.left_motor_backward , speed)
        self.motor.MotorRun(self.right_motor, self.right_motor_backward , speed)
        time.sleep(timeout)

    def set_left(self, speed=100,timeout=2):
        self.motor.MotorRun(self.left_motor, self.left_motor_forward , speed)
        time.sleep(timeout)
    def set_right(self, speed=100,timeout=2):
        self.motor.MotorRun(self.right_motor, self.right_motor_forward , speed)
        time.sleep(timeout)
        
    def turn_cw(self, speed=100,timeout=2):
        self.motor.MotorRun(self.left_motor, self.left_motor_forward , speed)
        self.motor.MotorRun(self.right_motor, self.right_motor_backward , speed)
        time.sleep(timeout)

    def turn_ccw(self, speed=100,timeout=2):
        self.motor.MotorRun(self.right_motor, self.right_motor_forward , speed)
        self.motor.MotorRun(self.left_motor, self.left_motor_backward , speed)
        time.sleep(timeout)
    
    def stop(self):
        self.motor.MotorStop(self.left_motor)
        self.motor.MotorStop(self.right_motor)


Driver = MotorDriver()
Motor = MotionController(Driver)

#test

Motor.turn_cw(30,3)
Motor.stop()
Motor.turn_ccw(30,3)
Motor.stop()