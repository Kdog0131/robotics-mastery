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

fleet = [robot_1, robot_2, robot_3, robot_4, robot_5] #Here I made a fleet variable and inside it I have it store a list which holds the five robot objects.




for robot in fleet: #Here I made a for loop with a loop variable named robot and have it specifically use the fleet variable and the list its storing.
    print(robot.name, robot.x, robot.y, robot.front_sensor) #Here I make a print statement that will print out each robots name, x coordinate value, y coordinate value, front_sensor value and name.


warned_robots = set() #Here I made a warned_robots variable and inside of it I have it store an empty set.

for robot in fleet: #Here I made a for loop with a loop variable named robot that will go through the entire list that the fleet variable is holding.
    filename = robot.name + "_log.txt" #Here I made a filename variable and inside it I have the robot object use its named attribute and have a string "_log.txt".
    with open(filename, "w") as f: #Here I made a with open that has the filename variable as its parameter and have it be in "w" mode so that it resets the text file everytime the program is runned, I also have it be represented as the variable f.
        f.write("") #Here I have the with open use the write function to write "" in the file.



for i in range(5): #Here I made a for loop with a loop variable named i and set the range to 5 so that anything inside the for loop will loop five times.
    for robot in fleet: #Here I made a for loop with a loop variable named robot and have it specifically use the fleet variable and the list its storing.
        
        robot.front_sensor = robot.front_sensor - (i * 0.2) #Here I have the robot object refer to its own front_sensor and then we take the increment number represented by i multiplied by 0.2 and subtract ot from the robots front_sensor value.

        is_danger, sensor_value = robot.check_obstacle() #Here I make a is_danger variable and a sensor_value variable and inside both I have the robot object called the check_obstacle method so that both variables take the value from the check_obstacle() method being called.
        
        filename = robot.name + "_log.txt" #Here I made a filename variable and I have it set to the robot objects name and a string called _log.text to help with identifiying  each robot object that is tied to a different textfile.

        #Here I made a with open that uses the filename variable and have it be in "a" mode and is represented by f.
        with open(filename, "a") as f:
            f.write(robot.name + " Tick: " + str(i) + " Sensor: " + str(round(robot.front_sensor, 2)) + " Danger: " + str(is_danger) + "\n") #Here I have the file write the robot objects name, the increment number converted to a string, the front_sensor values rounded number two decimal places converted into a string, the is_danger variable and \n so that the information is printed on a new line every increment.
        
        #Here I made an if statement that uses the is_danger method, it will add a the robot objects name to the warned_robots set everytime is_danger is read.
        if is_danger:
            warned_robots.add(robot.name)

        print(robot.name, "Tick ", i, "- Sensor: ", round(robot.front_sensor, 2), "- Danger: ", is_danger) #Here I made a print statement that will print out the robots name, "Tick", the increment number represented by i, the robots front_sensor value rounded two decimal places, "- Danger" and the condition of whather or not a robot is in danger of collision which will be true or false.

print("Total robots in fleet:", len(fleet)) #Here I made a print that prints out the total number of robots in the entire fleet list.

print("Robots that triggered a warning:", warned_robots) #Here I made a print statement that will show all of the robots that were warned in the set.

#Here I made a try/except block so that I can create the functionality for when the Guard_log.txt file is being read and the error that will be thrown of it cant be read.
try:
    with open("Guard_log.txt", "r") as f: #Here I made a with open that will open the Guard_log.txt file in "r" mode and have it be represented as the variable f.
        contents = f.read() #Here I made a contents variable and inside of it I have the file read itself using the read function.
        print(contents) #Here I made a print statement that will print that the contents variable is storing which is everything being read in the Guard_log file.
except Exception as e: #Here in the except clause I have the exception be represented by e.
    print("Could not read the log file", e) #Here I made a Print that will tell the user the file could not be read.
