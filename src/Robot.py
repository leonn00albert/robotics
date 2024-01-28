from Motor import MotionController

from encoder_counter import EncoderCounter

class Robot():
    def __init__(self):
        self.left_encoder = EncoderCounter(pin_number=4)
        self.right_encoder = EncoderCounter(pin_number=26)
        self.motor = MotionController()
        self.left_encoder.stop()
        self.right_encoder.stop()


