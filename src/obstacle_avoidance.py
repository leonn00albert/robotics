from Robot import Robot
from time import sleep

class ObstacleAvoidance:
    def __init__(self, bot):
        self.robot = bot
        self.speed = 50
        self.direction = 1
    
    def get_motor_direction(self, distance):
        if distance >= 1:
            nearest_speed = self.speed
            furthest_speed = self.speed
            direction = 1
            delay = 100
        elif distance > 0.5:
            nearest_speed = self.speed
            furthest_speed = self.speed * 0.8
            direction = 1
            delay = 100
        elif distance > 0.2:
            nearest_speed = self.speed
            furthest_speed = self.speed * 0.6
            direction = 1
            delay = 100
        elif distance > 0.1:
            nearest_speed = self.speed * 0.4
            furthest_speed = self.speed 
            direction = 0
            delay = 100  
        else: # collision
            nearest_speed = self.speed
            furthest_speed = self.speed 
            direction = 0
            delay = 250  
        return nearest_speed, furthest_speed, direction, delay


    def run(self):
        #self.robot.set_pan(0)
        #self.robot.set_tilt(0)

        while True:
            left_distance = self.robot.left_distance_sensor.distance
            right_distance = self.robot.right_distance_sensor.distance

            print("left: {l:.2f}, Right{r:.2f}".format(l=left_distance  * 100, r=right_distance * 100,))

            nearest_speed, furthest_speed, direction, delay = self.get_motor_direction(min(left_distance,right_distance))

            if( left_distance < right_distance):
                self.robot.motor.set_left(nearest_speed,direction)
                self.robot.motor.set_right(furthest_speed,direction)
            else:
                self.robot.motor.set_left(furthest_speed,direction)
                self.robot.motor.set_right(nearest_speed,direction)

            sleep(delay * 0.001)

bot = Robot()
avoid = ObstacleAvoidance(bot)
avoid.run()