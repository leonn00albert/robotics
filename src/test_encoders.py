import time 
import logging
import MotionController from Motor
import MotorDriver from Motor

from gpiozero import DigitalnputDevice
logger = logging.getLogger('test_encoders')

class EncoderCounter(object):
    def __init__(self, pin_number):
        self.pulse_count = 0
        self.device = DigitalnputDevice(pin=pin_number)
        self.device.pin.when_changed = self.when_changed

    def when_changed(self, _, state):
        self.pusle_count += 1


stop_at_time = time.time() +1

logging.basicConfig(level-logging.INFO)

Driver = MotorDriver()
Motor = MotionController(Driver)

#test
left_encoder = EncoderCounter(4)
right_encoder = EncoderCounter(26
)

Motor.forward(40,5)
Motor.stop()


while time.time() < stop_at_time:

