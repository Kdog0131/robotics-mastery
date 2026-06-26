
import math

def move_robot(x, y, theta_degrees, d):
    theta_rad = math.radians(theta_degrees)
    delta_x = d * math.cos(theta_rad)
    delta_y = d * math.sin(theta_rad)
    new_x = x + delta_x
    new_y = y + delta_y
    return new_x, new_y


print("=== Robot making 5 moves ===")
x = 0.0
y = 0.0

for i in range(5):
    x, y = move_robot(x, y, 0, 2)
    print("Step", i, "-> position:", round(x, 3), round(y, 3))


print("\n=== Robot moving until x reaches 10 ===")
x = 0.0
y = 0.0
steps = 0

while x < 10:
    x, y = move_robot(x, y, 0, 0.5)
    steps = steps + 1
    print("Step", steps, "-> position:", round(x, 3), round(y, 3))

print("Reached x =", round(x, 3), "in", steps, "steps")

