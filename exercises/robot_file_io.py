# PSEUDOCODE PLAN - Lesson 13: File I/O
# 1. Create a Robot with name, x, y, and front sensor
# 2. Write the robot's starting position to robot_log.txt
# 3. Simulate front sensor updating to a new value
# 4. Append the new sensor reading to robot_log.txt
# 5. Read robot_log.txt and print everything in it.

class Robot:
    def __init__(self, name, x, y, front_sensor):
        self.name = name
        self.x = x
        self.y = y
        self.front_sensor  = front_sensor

robot_1 = Robot("Scout", 0.0, 0.0, 5.2)

with open("robot_log.txt", "w") as f:
    f.write("Robot: " + robot_1.name + "\n")
    f.write("Starting positions: " + str(robot_1.x) + " " + str(robot_1.y) + "\n")
    f.write("Front sensor: " + str(robot_1.front_sensor) + "\n")

robot_1.front_sensor = 0.3

with open("robot_log.txt", "a") as f:
    f.write("Updated front sensor: " + str(robot_1.front_sensor) + "\n")

with open("robot_log.txt", "r") as f:
    contents = f.read()
    print(contents)
    

