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



    

