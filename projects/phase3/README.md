# Robot Path Simulator

A Python simulation that models a robot navigating through a series of 
waypoints. For each waypoint, the robot calculates the distance and 
direction to travel, moves accordingly, and its full path is plotted 
using matplotlib.

## How it works

- `get_distance_and_directions(dx, dy)` — calculates the distance and 
  direction (angle) the robot needs to travel to reach the next waypoint
- `rotate_then_move(x, y, direction, distance)` — rotates the robot to 
  face that direction, then moves it forward by the calculated distance

Both functions are imported from `trig_movement.py`, which contains 
the full trigonometry toolkit built throughout this project.

## Running it

1. Make sure Python is installed
2. Install matplotlib: `pip install matplotlib`
3. Make sure `trig_movement.py` is in the same folder as 
   `robot_simulator.py`
4. Run `robot_simulator.py` from your terminal or IDE

## Example output

The simulation plots the robot's full path from its starting position 
through each waypoint, with the start marked as a green square and 
waypoints marked as red triangles.
