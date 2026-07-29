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

def get_distance_and_directions(dx, dy): #Here I made a function named get_distance_and_directions with dx and dy in its parameters.
    magnitude = math.sqrt(dx**2 + dy**2) #Here I made a magnitude variable and inside it I have the math import use its sqrt function so that anything inside the parenteses will be squared, I put dx and dy in the parenteses and gave them both ** power operators so that they are squared aswell as + sign to add them both.
    direction = math.atan2(dy,dx) #Here I made a direction variable and inside it I have the math import use its atan2 function so that the program gives the angle and direction from dx and dy since we put dx and dy in the parenteses.
    direction_degrees = math.degrees(direction) # Here I made a direction_degrees variable and inside it I have the math import use its degrees functions so that the program will output the degrees using the direction variables information.
    return magnitude, direction_degrees #Here I made a return that returns the results of the magnitude and direction_degrees variable.

def rotate_point(x,y,theta_degrees): #Here I made a function named rotate_point with x,y and theta_degrees in its parameters.
    theta_radians = math.radians(theta_degrees) #Here I made a theta_radians variable and inside it I have the math import use its radians function with theta_degrees inside its parameters so that it can convert the number that theta_degrees has into radians.
    new_x = math.cos(theta_radians) * x - math.sin(theta_radians) * y #Here I made a new_x variable and inside it I have the math input use its cos function with theta_radians inside of it multipied by the number the x variable is holding, I then subtract that by the number that theta_radians is holding in the math imports sin function which is being multiplied by the number the y variable is holding.
    new_y = math.sin(theta_radians) * x + math.cos(theta_radians) * y #Here I made a new_y variable and inside it I have the math input use its sin function with theta_radians inside of it multipied by the number the x variable is holding, I then add that by the number that theta_radians is holding in the math imports cos function which is being multiplied by the number the y variable is holding.
    return new_x, new_y #Here I made a return statement that returns the results of the new_x and new_y variables calculations.

def rotate_then_move(x, y, theta_degrees, distance): #Here I made a function named rotate_then_move with x,y, theta_degrees and distance variables as its parameters/inputs.
    theta_radians = math.radians(theta_degrees) #Here I made a theta_radians variable and inside it I have the math import use its radians function with theta_degrees inside its parameters so that it can convert the number that theta_degrees has into radians.
    new_x = x + math.cos(theta_radians) * distance #Here I made a new_x variable and inside of it I have the number the x variable is holding added to the number theta_radians is holding which is converted to cos via the math import using its cos function, it then multiplys the result of that calculation with the number the distance variable is holding.
    new_y = y + math.sin(theta_radians) * distance #Here I made a new_y variable and inside of it I have the number the y variable is holding added to the number theta_radians is holding which is converted to sin via the math import using its sin function, it then multiplys the result of that calculation with the number the distance variable is holding.
    return new_x, new_y #Here I made a return statement that returns the results of the new_x and new_y variables calculations.


result_magnitude, result_direction = get_distance_and_directions(3, 4) #Here I chain the result_magnitude and result direction variables and have them equal the get_distance_and_directions function with 3 and 4 in its parameters so that both variables are tied to the result of the function call.
print("Magnitude:", round(result_magnitude,2)) #Here I made a print that prints Magnitude: and the magnitude result rounded 2 decimal places.
print("Direction (degrees): ", round(result_direction, 2)) #Here I made a print that prints Direction (degrees): and the direction result rounded 2 decimal places.
rotated_x, rotated_y = rotate_point(3, 0, 90) #Here I made a rotated_x variable and a rotated_y variable which are chained together and I have them both call the rotate_point function with 3 for x, 0 for y and 90 for what the theta_degrees.
print("Rotated point:", round(rotated_x, 2), round(rotated_y, 2)) #Here I made a print statement that prints "Routataed point:" and the the results of the new rotated x and y values rounded two decimal places.
final_x, final_y = rotate_then_move(0, 0, 90, 5) #Here I made a final_x and a final_y variable that are chained together and I have them call the rotate_then_move function with 0 for x, 0 for y, 90 for theta_degrees and 5 for distance.
print("Final position:", round(final_x, 2), round(final_y, 2)) #Here I made a print statement that prints "Final position" along with the new x and new y coordinate values rounded two decimal places.