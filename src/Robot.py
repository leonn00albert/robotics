from Motor import MotionController

from encoder_counter import EncoderCounter

class Robot():
    wheel_diameter_mm = 70.0
    ticks_per_revolution = 40.0
    wheel_distance_mm =  140.0

    def __init__(self):                                                   
   
        self.motor = MotionController()

        EncoderCounter.set_constants(self.wheel_diameter_mm, self.ticks_per_revolution)
        self.left_encoder = EncoderCounter(4)
        self.right_encoder = EncoderCounter(26)
