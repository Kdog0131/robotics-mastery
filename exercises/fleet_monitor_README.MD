# Multi-Robot Fleet Monitor

A Python program that simulates managing a fleet of 5 robots simultaneously, tracking each robot's sensor readings, checking for potential collisions, and logging each robot's status to its own individual file. Built as a follow-up to the single-robot Sensor Simulator, extending the same concepts to manage multiple robots at once.

## What it demonstrates

- Nested loops (a loop inside a loop) to check every robot on every simulated tick
- Classes and objects — 5 independent Robot instances managed as a group
- Sets — tracking which robots have ever triggered a collision warning, with automatic duplicate removal
- File I/O — each robot writes to its own separate log file
- Error handling (try/except) — protects file reads from crashing the program
- Conditional logic — obstacle detection based on a configurable threshold

## How it works

The program creates 5 `Robot` objects, each with a unique name, position, and front sensor reading, grouped into a single fleet list. Over a 5-tick simulated mission, the program loops through every robot on every tick, updates each one's sensor reading, and checks it against a safety threshold. Each robot's results are logged to its own file (e.g., `Guard_log.txt`), and a set collects the names of any robot that has ever triggered a warning — regardless of how many times. After the simulation ends, the program prints a final report: total robot count, which robots ever warned, and a sample log read back from disk.

## How to run it

1. Open a terminal (Git Bash or similar)
2. Navigate to the exercises folder: 
3. Run the program:

## What I'm proud of

Being able to simulate what it 
feels like to manage an entire 
fleet of robots at once — not just one — which mirrors real industrial use cases like 
routine maintenance monitoring across multiple machines. 
Watching the set correctly collapse five repeated warnings from 
one robot into a single entry made the concept of "has this ever happened" 
click in a way that felt genuinely useful, not just academic.
