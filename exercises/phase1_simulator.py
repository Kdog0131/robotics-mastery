# PHASE 1 PROJECT - Python Robot Sensor Simulator
# 1. Create a Robot with name, x, y, and front sensor
# 2. Run a loop for 5 ticks 
# 3. Each tick: Scan (update sensor), check for obstacle, log result to file
# 4. After all ticks: read the full log and print it.

#Here I made a class named Robot.
class Robot:

    def __init__(self,x,y,front_sensor, name): #Here I made a method named __init__ so that I can use it to create the attributes I want the class to have using the self keyword.
        
        self.x = x #Here I created a x attribute.
        self.y = y #Here I created a y attribute.
        self.front_sensor = front_sensor #Here I created a front_sensor attribute.
        self.name = name #Here I created a name attribute.

robot_1 = Robot(0.0, 0.0, 5.2, "Scout") #Here I made a Robot_1 variable and have it create a robot object with 0.0 as the x-coordinate, 0.0 for the y-coordinate, 5.2 for the front-sensor reading/distance, and Scout as the name.

print(robot_1.name, robot_1.x, robot_1.y, robot_1.front_sensor) #Here I made a print statement that prints the robots name, its two coordinates and the front sensor reading/distance.

#Here we make a for loop and have it increment 5 times.
for i in range(5):
    robot_1.front_sensor = 5.2 - (i * 0.3) #Inside the for loop we calculate a new sensor reading based on 5.2 minus a small amount each tick, and store that new value into the robot's front_sensor attribute. 
    print(robot_1.front_sensor) #Here we make a print statement to see the results of the subtraction after the five increments.
