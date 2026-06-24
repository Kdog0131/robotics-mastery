import math

def move_robot(x, y, theta_degrees, d):
    theta_rad = math.radians(theta_degrees)
    delta_x = d * math.cos(theta_rad)
    delta_y = d * math.sin(theta_rad)
    new_x = x + delta_x
    new_y = y + delta_y
    return new_x, new_y


result_x, result_y = move_robot(0, 0, 45, 4)
print("After move 1:", round(result_x, 3), round(result_y, 3))

result_x, result_y = move_robot(result_x, result_y, 90, 3)
print("After move 2:", round(result_x, 3), round(result_y, 3))

result_x, result_y = move_robot(result_x, result_y, 0, 5)
print("After move 3:", round(result_x, 3), round(result_y, 3))