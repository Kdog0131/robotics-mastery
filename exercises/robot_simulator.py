import matplotlib.pyplot as plt #Here I imported matplotlib.pylot as plit so that this program can graph coordinates.

from trig_movement import get_distance_and_directions, rotate_then_move #Here I import both the get_distance_and_directions and rotate_then_move functions from the trig_movement file so that they can be used in this file

start_x = 0 #Here I made a start_x variable and have it store the number zero to serve as the x-coordinate.
start_y = 0 #Here I made a start_y variable and have it store the number zero to serve as the y-coordinate.
waypoints = [(3, 4), (5, 1), (-2, 3)] #Here I made a waypoints variable and I have it store a list of tuples that serves as pairs of coordinates.

current_x = start_x #Here I make a current_x variable and have it store the number the start_x variable is storing.
current_y = start_y #Here I make a current_y variable and have it store the number the start_y variable is holding.
visited_x = [start_x] #Here I made a visited_x variable and have it store a list containing the number the start_x variable is holding.
visited_y = [start_y] #Here I made a visited_y variable and have it store a list containing the number the start_y variable is holding.

for waypoint in waypoints: #Here I made a for loop with waypoint as its loop variable name so that it can go therough th items in the waypoints variables list.
    target_x, target_y = waypoint #Inside the for loop I made a target_x and target_y variables that are chained together and I have them both set to the list the waypoint variable is holding.
    dx = target_x - current_x #Here I made a dx variable and inside it I have the number the target_x variable is holding subtract from the number the  current_x variable is holding.
    dy = target_y - current_y #Here I made a dy variable and inside it I have the number the target_y variable is holding subtract from the number the  current_y variable is holding.
    distance, direction = get_distance_and_directions(dx, dy) #Here I made a distance and direction variables that are chained togather and I have them both call the get_distance_and_directions function with the dx and dy variables as the functions parameters.
    current_x, current_y = rotate_then_move(current_x, current_y, direction, distance) #Here I made a current_x and current_y variables that are chained together and I have them both call the rotate_then_move function with the current_x, current_y, direction and distance variables as the functions parameters.
    visited_x.append(current_x) #Here I have the visited_x variable add the number the current_x variable is holding into the list its storing.
    visited_y.append(current_y) #Here I have visited_y variable add the number the current_y variable is holding into the list its storing.

plt.plot(visited_x, visited_y, 'o-') #Here I have matplotlib use its plot function with the numbers the visited_x and visited_y variables are holding as x and y coordinates respectivly and 'o-' so that it is drawn as a circle.
plt.show() #Here I have matplotlib use its show function to print out the coordinates