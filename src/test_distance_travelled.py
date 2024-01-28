import time 
import logging
import math
from Robot import Robot
from gpiozero import DigitalInputDevice

logger = logging.getLogger('test_distance_travelled')

wheels_diameter_mm = 70.0
ticks_per_revolution = 40.0
ticks_to_mm_const = (math.pi / ticks_per_revolution) * wheels_diameter_mm

def ticks_to_mm(ticks):
    return int(ticks_to_mm_const * ticks)

bot = Robot()
stop_at_time = time.time() +3

bot.motor.forward(30)


while time.time() < stop_at_time:
    print("Left:", ticks_to_mm(bot.left_encoder.pulse_count), "Right:", ticks_to_mm(bot.right_encoder.pulse_count))
    time.sleep(0.05)

bot.motor.stop()