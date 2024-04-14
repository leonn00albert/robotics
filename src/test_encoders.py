import time 
import logging
from Motor import MotionController
from Motor import MotorDriver
from gpiozero import DigitalInputDevice

logger = logging.getLogger('test_encoders')

class EncoderCounter(object):
    def __init__(self, pin_number):
        self.pulse_count = 0
        self.device = DigitalInputDevice(pin=pin_number)
        self.device.pin.when_changed = self.when_changed

    def when_changed(self, _, state):
        self.pulse_count += 1




Motor = MotionController()

#test
left_encoder = EncoderCounter(4)
right_encoder = EncoderCounter(26)

stop_at_time = time.time() +3

Motor.forward(30)


while time.time() < stop_at_time:
    print("Left:", left_encoder.pulse_count, "Right:", right_encoder.pulse_count)
    time.sleep(0.05)

Motor.stop()