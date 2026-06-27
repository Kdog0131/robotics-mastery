# PSEUDOCODE PLAN - Lesson 11: Lists and Dictionaries.
# 1. Create a dictionary storing 4 sensor readings by name.
# 2. Print all sensor readings.
# 3. Check if front sensor detects an obstacle (< 0.5m)
# 4. Simulate a sensor update (front gets a new reading)
# 5. Print updated readings.

#Here we make a sensors variable and have it store a dictionary with front,back,left and right keys.
sensors = {
    "front": 5.2,
    "back": 4.8,
    "left": 6.1,
    "right": 3.3

}

print(sensors) #Here we make a print and have it print whats in the sensors dictonary.

sensors["front"] = 0.3

if sensors["front"] < 0.5:
    print("Obstacle detected! Stopping robot.")
else:
    print("Path is clear.")


print("Updated front sensor:", sensors["front"])
