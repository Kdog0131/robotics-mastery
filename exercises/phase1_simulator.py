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

    def check_obstacle(self, threshold=0.5): #Here we made a check_obstacle method so that we can create a specific threshold condition for when a robot is about to collide with an object.
     if self.front_sensor < threshold: #If the front_sensors value as its decreacing is less then what the threshold variable is holding in the methods parameters, then it will return ethier false or true.
       return True, self.front_sensor
     else:
       return False, self.front_sensor
      
   
robot_1 = Robot(0.0, 0.0, 5.2, "Scout") #Here I made a Robot_1 variable and have it create a robot object with 0.0 as the x-coordinate, 0.0 for the y-coordinate, 5.2 for the front-sensor reading/distance, and Scout as the name.

print(robot_1.name, robot_1.x, robot_1.y, robot_1.front_sensor) #Here I made a print statement that prints the robots name, its two coordinates and the front sensor reading/distance.

with open("sensor_log.txt", "w") as f: #Here we create a file named sensor_log and have it be in "w" mode so that the file gets created and clears the readings each time the program is runned.
    f.write("")

#Here we make a for loop and have it increment 5 times.
for i in range(5):
    robot_1.front_sensor = 5.2 - (i * 0.3) #Inside the for loop we calculate a new sensor reading based on 5.2 minus a small amount each tick, and store that new value into the robot's front_sensor attribute. 
    print(round(robot_1.front_sensor, 2))#Here we make a print statement to see the results of the subtraction after the five increments, inside the print statement we use the round function and have front_sensor be placed in its argument along with a two so that only the firat two decimals will be shown in the output.
    with open("sensor_log.txt", "a") as f: #Here we open the sensor_readings file and have it be in "a" mode so that the for loop can keep adding to it.
        f.write("Tick: " + str(i) + " Sensor: " + str( round(robot_1.front_sensor, 2) ) + "\n") #Every time the for loop increments, we add the increment number and the reading from the front sensor and repeat on a new line every increment, we also convert the robot_1 objects front_sensor attribute into a string and have it be wrapped inside of the round functions parameters with a two so that only the first two decimals are printed.
    is_danger, sensor_value = robot_1.check_obstacle() #Here I make two variables named is danger and sensor_value and have them both be used as the values that check_obstacle stores, I then have the robot_1 object call the check_obstacle method which will return a true or false sensor reading.
    #This if statement checks to see if there is a collision based on the number the front_sensor value being decremented which is 5.2, etheir "No Collision detected" or "Warning collision detected" will be printed based on whether or not the decrementing number is less then 0.5, and the if/else block and the true condition helps to regulate that functionality.
    if is_danger == True:
     print("Warning Collision Imminent!")
    else:
       print("No Collision Detected")


#Here we use a try/except so that we can throw an error if the sensor_log file cannot be read or open.   
try:
 with open("sensor_log.txt", "r") as f: #Here we open sensor_log in "r" mode so that we can read what was sent to the file from the for loop.
    contents = f.read() #Here we make a contents variable and inside it we have the file use the read function read everything in it.
    print(contents) #Here we make a print statement and inside it have the contents variable in its argument so that it prints out what the file recorded.
except Exception as e:
    print("Could not read the log file", e) #This is the error that will be thrown in the except block.


    