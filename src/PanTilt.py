from time import sleep
from gpiozero import AngularServo
class PanTilt:
    def __init__(self, pan_pin, tilt_pin, min_angle=-90, max_angle=90, min_pulse_width=0.0006, max_pulse_width=0.0023):
        self.pan_servo = AngularServo(pan_pin, min_angle=min_angle, max_angle=max_angle, min_pulse_width=min_pulse_width, max_pulse_width=max_pulse_width)
        self.tilt_servo = AngularServo(tilt_pin, min_angle=min_angle, max_angle=max_angle, min_pulse_width=min_pulse_width, max_pulse_width=max_pulse_width)

    def pan(self, angle):
        self.pan_servo.angle = angle

    def tilt(self, angle):
        self.tilt_servo.angle = angle

    def move_servo_smoothly(self, servo, target_angle, duration=1, steps=10):
        current_angle = servo.angle
        angle_change = target_angle - current_angle
        step_angle = angle_change / steps

        for _ in range(steps):
            current_angle += step_angle
            servo.angle = current_angle
            sleep(duration / steps)


