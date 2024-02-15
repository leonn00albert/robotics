from Robot import Robot
from time import sleep

class ObstacleAvoidance:
    def __init__(self, bot):
        self.robot = bot
        self.speed = 60
        self.direction = 1
        self.reverse_count = 0  # Initialize reverse count
    
    def get_motor_direction(self, distance):
        action = ''
        if distance >= 1:
            self.reverse_count = 0  # Reset reverse count
            nearest_speed = self.speed
            furthest_speed = self.speed
            direction = 1
            delay = 100
            action = 'move'
        elif distance > 0.5:
            self.reverse_count = 0  # Reset reverse count
            nearest_speed = self.speed
            furthest_speed = self.speed * 0.8
            direction = 1
            delay = 100
            action = 'move'
        elif distance > 0.2:
            self.reverse_count = 0  # Reset reverse count
            nearest_speed = self.speed
            furthest_speed = self.speed * 0.6
            direction = 1
            delay = 100
            action = 'move'
        elif distance > 0.1:
            self.reverse_count += 1
            nearest_speed = 40
            furthest_speed = 100
            direction = 0
            delay = 100
            action = 'turn'
        else: # distance <= 0.1, reverse
            nearest_speed = self.speed  # Reverse speed
            furthest_speed = self.speed 
            direction = 0
            delay = 100  
            action = 'reverse'
            self.reverse_count += 1  # Increment reverse count
            if self.reverse_count >= 5:  # Check if 5 reverses have been done
                self.reverse_count = 0  # Reset reverse count
                action = '180_turn'  # Perform 180-degree turn
        
        return nearest_speed, furthest_speed, direction, delay, action

    def run(self):
        #self.robot.set_pan(0)
        #self.robot.set_tilt(0)

        while True:
            left_distance = self.robot.left_distance_sensor.distance
            right_distance = self.robot.right_distance_sensor.distance

            print("left: {l:.2f}, Right: {r:.2f}".format(l=left_distance * 100, r=right_distance * 100))

            nearest_speed, furthest_speed, direction, delay, action = self.get_motor_direction(min(left_distance, right_distance))

            # Making hard turns away from obstacles or reversing
            if left_distance < right_distance:
                if action == 'turn':
                    self.robot.motor.set_left(nearest_speed, 1 - direction)
                    self.robot.motor.set_right(furthest_speed,  direction)  # Opposite direction
                elif action == '180_turn':
                    self.robot.motor.set_left(self.speed, 1)
                    self.robot.motor.set_right(self.speed, 0)  # 180-degree turn
                    sleep(0.5)
                else:
                    self.robot.motor.set_left(nearest_speed, direction)
                    self.robot.motor.set_right(furthest_speed, direction)  # Opposite direction
            else:
                if action == 'turn':
                    self.robot.motor.set_left(furthest_speed,  direction)  # Opposite direction
                    self.robot.motor.set_right(nearest_speed, 1- direction)
                elif action == '180_turn':
                    self.robot.motor.set_left(self.speed, 0)
                    self.robot.motor.set_right(self.speed, 1)  # 180-degree turn
                    sleep(0.5)
                else:
                    self.robot.motor.set_left(furthest_speed, direction)  # Opposite direction
                    self.robot.motor.set_right(nearest_speed, direction)

            sleep(delay * 0.001)

bot = Robot()
avoid = ObstacleAvoidance(bot)
avoid.run()
