# PILLER 1 - Trigonometry for Robot Movement.
# 1. Import the math module.
# 2. Define a robots starting position (x, y) and facing angle (theta) in degrees.
# 3. Convert theta from degrees to radians.
# 4. calculate new_x and new_y using cos(theta) and sin(theta).
# 5. Print the robot's new Position.

import math #Here I import the math module so that I can use pythons math functions in this program.

x = 0.0 #Here I made an x variable and inside it I have it store the decimal number 0.0.
y = 0.0 #Here I made an y variable and inside it I have it store the decimal number 0.0.
theta_degrees = 90 #Here I made a theta_degrees variable and have it store the number 90.
distance = 1.0 #Here I make a distance variable and have ist store the number 1.0.

theta_radians = math.radians(theta_degrees) #Here I made a theta_radians variable and inside of it, I have the math module use the radians function with the theta_degrees variable in its parameters so that we can convert the number the theta_degrees variable is holding into radians.

new_x = x + math.cos(theta_radians) * distance #Here I make a new x variable and inside of it I have the x variable add the cosine value of theta_radians and multiply that by the number the distance variable is holding, which is 1.0.
new_y = y + math.sin(theta_radians) * distance #Here I make a new y variable and inside of it I have the y variable add the sin value of theta_radians and multiply that by the number the distance variable is holding, which is 1.0.



print(round(theta_radians, 2)) #Here I make a print statement that will print out the number that the theta_radians variable is holding, I also wrapped the theta_radians variable inside of a round, so that the number printed will be rounded 2 decimal places as designated by the 2.


print("New position:", round(new_x, 2), round(new_y, 2)) #Here I make a print statement that prints New Position and the new x and y coordinate numbers that are rounded two decimal places.

