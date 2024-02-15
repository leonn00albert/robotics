from Motor import MotionController
from status import Status
from encoder_counter import EncoderCounter
from drive import Drive
from gpiozero import DistanceSensor

class Robot():
    wheel_diameter_mm = 70.0
    ticks_per_revolution = 40.0
    wheel_distance_mm =  140.0

    def __init__(self):                                                   
        self.status = Status()
        self.motor = MotionController()
        EncoderCounter.set_constants(self.wheel_diameter_mm, self.ticks_per_revolution)
        self.left_encoder = EncoderCounter(4)
        self.right_encoder = EncoderCounter(26)
        self.drive = Drive(self)
        self.left_distance_sensor = DistanceSensor(echo=17, trigger= 27, queue_len=2)
        self.right_distance_sensor = DistanceSensor(echo=5, trigger= 6, queue_len=2)


