# Robot Sensor Simulator 

A Python program that simulates a robot's front sensor detecting obstacles over time, logs each reading to a file, and reads back the full mission report. Built as part of a self-directed robotics engineering study path.

## What it demonstrates

- Object-oriented programming (Python classes)
- For loops and iterative logic
- File I/O (write, append, and read modes)
- Conditional logic for obstacle detection
- Floating point formatting with `round()`

## How it works

The program creates a `Robot` object with a name, position, and front sensor reading. Over a 5-tick simulated mission, the sensor value gradually decreases (simulating an obstacle getting closer). Each tick checks whether the reading is below a safety threshold, prints a warning if so, and logs the tick number and reading to `sensor_log.txt`. After the mission ends, the full log is read back and printed.

## How to run it

1. Open a terminal (Git Bash or similar)
2. Navigate to the exercises folder:
3. Run the program:
4. View the generated log file:

## What I'm proud of

Figuring out the math behind the sensor simulation myself — calculating how the sensor value should decrease each tick using the formula `5.2 - (i * 0.3)` — was the piece that made this feel like real robotics logic instead of just a coding exercise.
