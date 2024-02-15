from Robot import Robot
from time import sleep

class ObstacleAvoidance:
    def __init__(self, bot):
        self.robot = bot
        self.speed = 40
        self.direction = 1
    
    def get_motor_direction(self, distance):
        if distance < 0.2:
            
            return  0

        else:
           
            return 1

    def run(self):
        #self.robot.set_pan(0)
        #self.robot.set_tilt(0)

        while True:
            left_distance = self.robot.left_distance_sensor.distance
            right_distance = self.robot.right_distance_sensor.distance

            print("left: {l:.2f}, Right{r:.2f}".format(l=left_distance  * 100, r=right_distance * 100,))

            left_direction = self.get_motor_direction(left_distance)
            self.robot.motor.set_left(self.speed, left_direction)
            right_direction = self.get_motor_direction(right_distance)
            self.robot.motor.set_right(self.speed, left_direction)
            sleep(0.05)

bot = Robot()
avoid = ObstacleAvoidance(bot)
avoid.run()