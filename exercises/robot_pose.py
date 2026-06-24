import math

robot_x = 0.0
robot_y = 0.0
theta_degrees = 30.0
d = 6.0

theta_rad = math.radians(theta_degrees)

delta_x = d * math.cos(theta_rad)
delta_y = d * math.sin(theta_rad)

robot_x = robot_x + delta_x
robot_y = robot_y + delta_y

print("Robot moved!")
print("New x:", round(robot_x, 3))
print("New y:", round(robot_y, 3))
print("Facing:", theta_degrees, "Degrees")

