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

def rotate_shape(points, theta_degrees): #Here I made a function named rotate_shape with the points and theta_degrees variables ad its parameters/inputs.
    rotated_points = [] #Here I made a rotated_points variable and inside it I have it store and empty list which is where the rotated points will be added to overtime. 
    for x, y in points: #Here I made a for loop that will look the points and inspect the x and y variables in each tuple since they are chained together.
        new_x, new_y = rotate_point(x, y, theta_degrees) #Here I made new_x and new_y variables that are chained together and I have them both call rotate_point with the x,y and theta_degrees variables in its parameters.
        rotated_points.append((new_x, new_y)) #Here I have the rotated_points list add the numbers that the new_x and new_y variables are holding.
    return rotated_points #Here I made a return statement that returns the values that are in the list the rotated_points variable is storing.

def get_3d_magnitude(dx,dy,dz): #Here I made a function named get_3d_magnitude with dx, dy and dz variables as its parameters/inputs
    magnitude = math.sqrt(dx**2 + dy**2 + dz**2) #Here I made a magnitude variable and inside of it I have the math import use its square root function and inside of it I have the numbers that the dx,dy and dz variables are holding be to the second power, aswell as add them all together.
    return magnitude #Here I made a return statement that returns the results of the magnitude variables calculations.

def get_3d_direction(dx, dy, dz): #Here I made a function named get_3d_directions with dx,dy and dz variables as its parameters/inputs.
    azimuth = math.atan2(dy, dx) #Here I made an azimuth variable and inside of it I have the math import use its atan2 function with the dy and dx variables inside of its argument so that we can get the direction of the numbers the two variables are holding.
    elevation = math.atan2(dz, math.sqrt(dx**2 + dy**2)) #Here I made a elevation variable and inside it I have the math imprt use its atan2 function with the dz variable and the math import using its square root function with the dx and dy variables numbers to the second power inside of it.
    return azimuth, elevation #Here I made a return statement that returns the result of the azimuth and elevation variables calculations.

def rotate_point_z(x, y, z, theta_degrees): #Here I made a function named rotate_point_z with x, y, z and theta_degrees variables as its parameters/inputs.
    theta_radians = math.radians(theta_degrees) #Here I made a theta_radians variable and inside of it I have the math import use the radians function with the theta_degrees variable inside of it so that the number the theta_degrees variable is holding will be converted into radians.
    new_x = math.cos(theta_radians) * x - math.sin(theta_radians) * y #Here I made a new_x variable and inside of it I have the math import use its cos function with the theta_degrees variable inside of it so that the number the theta_degrees variable is holding will be converted into cos and have it be multiplied by x. I then subtract that result by the number the sin of the number that theta_radians is holding times y.
    new_y = math.sin(theta_radians) * x + math.cos(theta_radians) * y #Here I made a new_y variable and inside of it I have the math import use its cos function with the theta_degrees variable inside of it so that the number the theta_degrees variable is holding will be converted into sin and have it be multiplied by x. I then add that result by the number the cos of the number that theta_radians is holding times y.
    new_z = z #Here I made a new_z variable and I have it store the variable z so that it remains the same.
    return new_x, new_y, new_z #Here i made a return statement that returns the results of the new_x, new_y and new_z variables calculations.

def rotate_point_x(x, y, z, theta_degrees): #Here I made a function named rotate_point_x with x, y, z and theta_degrees variables as its parameters/inputs.
    theta_radians = math.radians(theta_degrees) #Here I made a theta_radians variable and inside of it I have the math import use its radians function with the theta_degrees variable inside of it so that it converts the number the theta_degrees variable is holding from degrees to radians.
    new_y = math.cos(theta_radians) * y - math.sin(theta_radians) * z #Here I made a new_y variable and inside of it I have the math import use its cos function with theta_radians inside of it so that it converts the number that theta_radians has into cos and multiply it by the number the y variable is holding, I then have that first result be subtracted by the sin version of the number theta_radians is holding and being multiplied by z. 
    new_z = math.sin(theta_radians) * y + math.cos(theta_radians) * z #Here I made a new_z variable and inside of it I have the math import use its sin function with theta_radians inside of it so that it converts the number that theta_radians has into sin and multiply it by the number the y variable is holding, I then have that first result be added by the cos version of the number theta_radians is holding and being multiplied by z. 
    new_x = x #Here I made a new_x variable and I have it store the number the x variable is holding.
    return new_x, new_y, new_z #Here I make a return statement that returns the result of the new_x, new_y and new_z variables calculations.


def rotate_point_y(x, y, z, theta_degrees): #Here I made a function named rotate_point_y with x, y, z and theta_degrees variables as it's parameters/inputs.
    theta_radians = math.radians(theta_degrees) #Here I made a theta_radians variable and inside of it I have the math import use its radians function with the theta_degrees variable inside of its argument so that it converts the number the theta_degrees variable is holding into radians.
    new_z = math.cos(theta_radians) * z - math.sin(theta_radians) * x #Here I make a new_z variable and inside of it I have the math import use its cos function to convert the number that the theta_radians variable is holding in to cos and have it be multiplied by the number the z variable is holding, I then take that result and subtract it from the sin version of the number the theta_radians variable is holding multiplied by the number the x variable is holding.
    new_x = math.sin(theta_radians) * z + math.cos(theta_radians) * x #Here I make a new_x variable and inside of it I have the math import use its sin function to convert the number that the theta_radians variable is holding in to cos and have it be multiplied by the number the z variable is holding, I then take that result and add it from the cos version of the number the theta_radians variable is holding multiplied by the number the x variable is holding.
    new_y = y #Here I made a new_y variable and I have it store the number the y variable is holding.
    return new_x, new_y, new_z #Here I made a return statement that resturns the results of the new_x, new_y and new_z variables.



result_magnitude, result_direction = get_distance_and_directions(3, 4) #Here I chain the result_magnitude and result direction variables and have them equal the get_distance_and_directions function with 3 and 4 in its parameters so that both variables are tied to the result of the function call.
print("Magnitude:", round(result_magnitude,2)) #Here I made a print that prints Magnitude: and the magnitude result rounded 2 decimal places.
print("Direction (degrees): ", round(result_direction, 2)) #Here I made a print that prints Direction (degrees): and the direction result rounded 2 decimal places.
rotated_x, rotated_y = rotate_point(3, 0, 90) #Here I made a rotated_x variable and a rotated_y variable which are chained together and I have them both call the rotate_point function with 3 for x, 0 for y and 90 for what the theta_degrees.
print("Rotated point:", round(rotated_x, 2), round(rotated_y, 2)) #Here I made a print statement that prints "Routataed point:" and the the results of the new rotated x and y values rounded two decimal places.
final_x, final_y = rotate_then_move(0, 0, 90, 5) #Here I made a final_x and a final_y variable that are chained together and I have them call the rotate_then_move function with 0 for x, 0 for y, 90 for theta_degrees and 5 for distance.
print("Final position:", round(final_x, 2), round(final_y, 2)) #Here I made a print statement that prints "Final position" along with the new x and new y coordinate values rounded two decimal places.
square = [(1, 0), (0, 1), (-1, 0), (0, -1)] #Here I made a square variable and inside it I have it store a list of different tupples for the points on the square.
rotated_square = rotate_shape(square, 90) #Here I made a rotated square variable and inside it I have it call the rotate_shape function with the square variable for the points using the tupples in the list the square variable is holding, and 90 for the theta_degrees in the functions parameters/inputs.
print("Rotated square:", rotated_square) #Here I made a print statement that prints "Rotated square" and the number that the rotated square variable is holding which will be the tupples in the square variables list.
result_3d = get_3d_magnitude(2, 3, 6) #Here I made a result_3d variable and inside it I have it call the get_3d_magnitude function with 2 as dx, 3 as dy and 6 as dz.
print("3D Magnitude:", round(result_3d, 2)) #Here I made a print statement that prints "3D Magnitude:" and the number that the result_3d variable is holding rounded two decimal places.
result_azimuth, result_elevation = get_3d_direction(0, 0, 5) #Here I made a result_azimuth and result_elevation variables that are chained together, and I have them both call the get_3d_direction method with 0 as dx, 0 as dy and 5 as dz.
print("Azimuth (degrees):", round(math.degrees(result_azimuth), 2)) #Here I made a print statement that prints "Azimuth (degrees):" and the number the rezult_azimuth variable is holding rounded two decimal places.
print("Elevation (degrees):", round(math.degrees(result_elevation), 2)) #Here I made a print statement that prints "Elevation (degrees):" and the number the rezult_elevation variable is holding rounded two decimal places.
rotated_x, rotated_y, rotated_z = rotate_point_z(3, 0, 7, 90) #here I made a rotated_x variable, a rotated_y variable and a rotated_z variable chained together, and I have them call the rotate_point_z method with 3 as x, 0 as y, 7 as z and 90 as theta_degrees.
print("Rotated point (z-axis):", round(rotated_x, 2), round(rotated_y, 2), round(rotated_z, 2)) #Here I made a print statement that prints "Rotated point(z-axis):" and the calculated numbers of the rotated_x, rotated_y and rotated_z variables rounded two decimal places.
rotated_x, rotated_y, rotated_z = rotate_point_x(7, 3, 0, 90) #Here I made a rotated_x, roatated_y and roatated_z variables that are chained together, and I have them all call the rotated_point_x function with 7 as x, 3 as y, 0 as zero and 90 as theta_degrees.
print("Rotated point (x-axis):", round(rotated_x, 2), round(rotated_y, 2), round(rotated_z, 2)) #Here I made a print statement that prints "Rotated point (x-axis):" and the results of the rotated_x, rotated_y and rotated_z variables calculations rounded two decimal places. 
rotated_x, rotated_y, rotated_z = rotate_point_y(0, 7, 3, 90) #Here I made a roated_x, rotated_y and rotated_z variables that are chained togather, and I have them call the rotate_point_y function with 0 for x, 7 for y, 3 for z and 90 for theta_degrees.
print("Rotated point (y-axis):", round(rotated_x, 2), round(rotated_y, 2), round(rotated_z, 2)) #Here I made a print statement that prints "Rotated point (y-axis):" and the results of the rounded_x, rounded_y and rounded_z variables calculations rounded two decimal places.