from pid_controller import PIController
import time
import logging
import math
from encoder_counter import EncoderCounter
logger = logging.getLogger("drive_distance")
class Drive():
    def __init__(self,bot):
        self.bot = bot;         
    def distances(self,left_distance, right_distance, speed=60,backward=1):

        if abs(left_distance) >= abs(right_distance):
            print("Left is primary")
            set_primary        = self.bot.motor.set_left
            primary_encoder    = self.bot.left_encoder
            set_secondary      = self.bot.motor.set_right
            secondary_encoder  = self.bot.right_encoder
            primary_distance   = left_distance
            secondary_distance = right_distance
        else:
            print("right is primary")
            set_primary        = self.bot.motor.set_right
            primary_encoder    = self.bot.right_encoder
            set_secondary      = self.bot.motor.set_left
            secondary_encoder  = self.bot.left_encoder
            primary_distance   = right_distance
            secondary_distance = left_distance



        primary_to_secondary_ratio = secondary_distance / (primary_distance * 1.0)
        secondary_speed = speed * primary_to_secondary_ratio


        primary_encoder.reset()
        secondary_encoder.reset()
        
        controller = PIController(proportional_constant=4, integral_constant=0.2)

        # Ensure that the encoder knows which way it is going
        primary_encoder.set_direction(math.copysign(1, speed))
        secondary_encoder.set_direction(math.copysign(1, secondary_speed))
        set_primary(speed)
        set_secondary(secondary_speed)

        while abs(primary_encoder.pulse_count) < abs(primary_distance) or abs(secondary_encoder.pulse_count) < abs(secondary_distance):        
            time.sleep(0.02)
            secondary_target = primary_encoder.pulse_count * primary_to_secondary_ratio
            error = secondary_target - secondary_encoder.pulse_count
            adjustment = controller.get_value(error)
            set_primary(speed - adjustment)

            secondary_encoder.set_direction(math.copysign(1, secondary_speed+adjustment))
            set_secondary(secondary_speed + adjustment)

            print(f"Encoders : primary: {primary_encoder.pulse_count}, secondary: {secondary_encoder.pulse_count}" )
            print(f"Distances : primary: {primary_encoder.distance_in_mm()}, secondary: {secondary_encoder.distance_in_mm()}" )

            if abs(primary_encoder.pulse_count) >= abs(primary_distance):
                print("primary stop")
                set_primary(0)
                secondary_speed = 0

    def arc(self, turn_in_degrees, radius, speed=80):
        """ Turn is based on change in heading. """
        # Get the bot width in ticks
        half_width_ticks = EncoderCounter.mm_to_ticks(self.bot.wheel_distance_mm/2.0)
        if turn_in_degrees < 0:
            left_radius     = radius - half_width_ticks
            right_radius    = radius + half_width_ticks
        else:
            left_radius     = radius + half_width_ticks
            right_radius    = radius - half_width_ticks
        print ("Arc left radius {:.2f}, right_radius {:.2f}".format(left_radius, right_radius))
        radians = math.radians(abs(turn_in_degrees))
        left_distance = int(left_radius * radians)
        right_distance = int(right_radius * radians)
        print ("Arc left distance {}, right_distance {}".format(left_distance, right_distance))
        self.distances(left_distance, right_distance, speed=speed)

    def distances_backward(self,left_distance, right_distance, speed=-60):

        if abs(left_distance) >= abs(right_distance):
            print("Left is primary")
            set_primary        = self.bot.motor.set_left
            primary_encoder    = self.bot.left_encoder
            set_secondary      = self.bot.motor.set_right
            secondary_encoder  = self.bot.right_encoder
            primary_distance   = left_distance
            secondary_distance = right_distance
        else:
            print("right is primary")
            set_primary        = self.bot.motor.set_right
            primary_encoder    = self.bot.right_encoder
            set_secondary      = self.bot.motor.set_left
            secondary_encoder  = self.bot.left_encoder
            primary_distance   = right_distance
            secondary_distance = left_distance



        primary_to_secondary_ratio = secondary_distance / (primary_distance * 1.0)
        secondary_speed = speed * primary_to_secondary_ratio


        primary_encoder.reset()
        secondary_encoder.reset()
        
        controller = PIController(proportional_constant=4, integral_constant=0.2)

        # Ensure that the encoder knows which way it is going
        primary_encoder.set_direction(math.copysign(1, speed))
        secondary_encoder.set_direction(math.copysign(1, secondary_speed))
        set_primary(speed)
        set_secondary(secondary_speed)

        while abs(primary_encoder.pulse_count) < abs(primary_distance) or abs(secondary_encoder.pulse_count) < abs(secondary_distance):        
            time.sleep(0.02)
            secondary_target = primary_encoder.pulse_count * primary_to_secondary_ratio
            error = secondary_target - secondary_encoder.pulse_count
            adjustment = controller.get_value(error)
            set_primary(speed - adjustment,-1)

            secondary_encoder.set_direction(math.copysign(1, secondary_speed+adjustment))
            set_secondary(secondary_speed + adjustment,-1)

            print(f"Encoders : primary: {primary_encoder.pulse_count}, secondary: {secondary_encoder.pulse_count}" )
            print(f"Distances : primary: {primary_encoder.distance_in_mm()}, secondary: {secondary_encoder.distance_in_mm()}" )

            if abs(primary_encoder.pulse_count) >= abs(primary_distance):
                print("primary stop")
                set_primary(0)
                secondary_speed = 0
