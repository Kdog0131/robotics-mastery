# PSEUDOCODE:
#Class Robot
# def __init__(Self, name, x,y front_sensor):
    # self.name = name
    # self.x = x
    # self.y = y
    # self.front_sensor = front_sensor


 # def check_obsticle(self):
       #if self.front_sensor < 0.5:
           #print("Warning: collision imminent")
       #else:
          #print("Path is clear")


 # def report_position(self):
     #Print(self.name, "is at", self.x,self.y)

class Robot:

    def __init__(self, name, x, y, front_sensor):
        self.name = name
        self.x = x
        self.y = y
        self.front_sensor = front_sensor

    def check_obstacle(self):
        if self.front_sensor < 0.5:
            print("Warning: collision detection imminent")
        else:
            print("Path is clear")

    def report_position(self):
        print(self.name + " is at " + str(self.x) + " " + str(self.y))


#Objects created using robot class
robot_1 = Robot("Scout", 0.0, 0.0, 5.2)
robot_1.report_position()
robot_1.check_obstacle()

robot_2 = Robot("Guard", 10.0, 5.0, 0.3)
robot_2.report_position()
robot_2.check_obstacle()