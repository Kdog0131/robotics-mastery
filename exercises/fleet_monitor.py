# PHASE 2 PROJECT - Multi-Robot Fleet Monitor
# 1. Create 5 Robot Objects (same class as Phase 1).
# 2. Run a fleet check loop for 5 ticks.
# 3. Each tick: loop through ALL robots, update sensor, check obstacle.
# 4. Each robot logs to its own file.
# 5. A set tracks names of robots that ever triggered a warning.
# 6. After all ticks: print final report (robot count, warned robots, sample log)

#Here I made a robot class
class Robot:
    #Here I made a init method inside the robot class so that I can create the attributes that each robot object will have.
    def __init__(self, x, y, front_sensor, name):
        self.x = x #Here I have self initalize x to itself.
        self.y = y #Here I have self initalize y to itself.
        self.front_sensor = front_sensor #Here I have self initalize front_sensor to itself.
        self.name = name #Here I have self initalize name to itself.
    
    #Here I made a check obstacle method with self and threshold as parameters so that I can make the functionality of creating a warning that the robot is going to collide with an object.
    def check_obstacle(self, threshold=0.5):
        #This if statement checks to see if the robot is within a certain threshold which defaults to 0.5 but can change. This will also return True or False depending on whether the robot is too close to an object.
        if self.front_sensor < threshold:
            return True, self.front_sensor
        else:
            return False, self.front_sensor 

robot_1 = Robot(2.5, 3.6, 1.0, "Scout") #Here I made a robot_1 object with 2.5 as the x coordinate value, 3.6 as the y coordinate value, 1.0 as the front sensor value and Scout as the name.
robot_2 = Robot(-1.5,-2.1, 0.0, "Guard") #Here I made a robot_2 object with -1.5 as the x coordinate value, -2.1 as the y coordinate value, 0.0 as the front sensor value and Guard as the name.
robot_3 = Robot(6.5, -1.9, 3.2, "Knight") #Here I made a robot_3 object with 6.5 as the x coordinate value, -1.9 as the y coordinate value, 3.2 as the front sensor value and Knight as the name.
robot_4 = Robot(7.2, 0.0, 2.5, "Archer") #Here I made a robot_4 object with 7.2 as the x coordinate value, 0.0 as the y coordinate value, 2.5 as the front sensor value and Archer as the name.
robot_5 = Robot(-1.1, -8.5, 5.0, "King") #Here I made a robot_5 object with -1.1 as the x coordinate value, -8.5 as the y coordinate value, 5.0 as the front sensor value and King as the name.

fleet = [robot_1, robot_2, robot_3, robot_4, robot_5] #Here i made a fleet variable and inside it I have it store a list which holds the five robot objects.

for robot in fleet: #Here I made a for loop with a loop variable named robot and have it specifically use the fleet variable and the list its storing.
    print(robot.name, robot.x, robot.y, robot.front_sensor) #Here I make a print statement that will print out each robots name, x coordinate value, y coordinate value, front_sensor value and name.

