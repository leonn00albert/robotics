from Robot import Robot, EncoderCounter
from pid_controller import PIController
import time
import logging
logger = logging.getLogger("drive_distance")

def drive_distance(bot, distance , speed=80):
    set_primary = bot.motor.set_left
    primary_encoder = bot.left_encoder
    set_secondary = bot.motor.set_right
    secondary_encoder = bot.right_encoder

    controller = PIController(proportional_constant=5, integral_constant=0.3)

    set_primary(speed)
    set_secondary(speed)

    while primary_encoder.pulse_count < distance or secondary_encoder.pulse_count < distance:
        time.sleep(0.01)
        error = primary_encoder.pulse_count - secondary_encoder.pulse_count
        adjustment = controller.get_value(error)
        set_primary(speed - adjustment)
        set_secondary(speed + adjustment)
        print(f"Encoders : primary: {primary_encoder.pulse_count}, secondary: {secondary_encoder.pulse_count}" )
        print(f"Distances : primary: {primary_encoder.distance_in_mm()}, secondary: {secondary_encoder.distance_in_mm()}" )

logging.basicConfig(level=logging.INFO)
bot = Robot()
distance_to_drive = 500
distance_in_ticks = EncoderCounter.mm_to_ticks(distance_to_drive)
drive_distance(bot,distance_in_ticks,50)
bot.motor.stop()