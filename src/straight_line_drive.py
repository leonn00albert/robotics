from Robot import Robot
from pid_controller import PIController
import time

bot = Robot()
time.sleep(1)
stop_at_time = time.time() + 4
speed = 40
bot.motor.set_right(speed)
bot.motor.set_left(speed)

pid = PIController(proportional_constant=5, integral_constant=0.3)
while time.time() < stop_at_time:
    time.sleep(0.02)
    # Calculate the error
    left = bot.left_encoder.pulse_count
    right = bot.right_encoder.pulse_count
    error = left - right
    # Get the speed
    adjustment = pid.get_value(error)
    left_speed = int(speed - adjustment)
    right_speed = int(speed + adjustment)
    print("left", left, \
        "right", right, \
        "right_speed:", right_speed, \
        "error:", error, \
        "adjustment: %.2f" % adjustment)
    # Appy it to the right motor
    bot.motor.set_right(right_speed)
    bot.motor.set_left(left_speed)

bot.motor.stop()