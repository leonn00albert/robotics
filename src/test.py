from Robot import Robot, EncoderCounter


bot = Robot()

distance_to_drive = 300/4
distance_in_ticks = EncoderCounter.mm_to_ticks(distance_to_drive)
radius = bot.wheel_distance_mm + 100
radius_in_ticks = EncoderCounter.mm_to_ticks(radius)

bot.status.ok()
bot.drive.distances(distance_in_ticks, distance_in_ticks)
bot.drive.distances(distance_in_ticks, distance_in_ticks)

bot.drive.arc(90,radius_in_ticks,70)

bot.status.info()
bot.motor.stop()