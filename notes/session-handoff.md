# Session Handoff — Robotics Roadmap

## Student
Name: Kelvin Marcano
GitHub: Kdog0131
Started: June 2026

## Teaching rules established
- Pre-session memory check every session
- Return ritual: active recall, no pre-reading
- 📓 NOTEBOOK for math and reference cards
- 💻 GITHUB for lesson notes in own words
- One command per line in terminal
- Pseudocode before coding starting Lesson 11
- Difficulty levels 1-4 on problems
- Projects at end of each phase

## Current position
Phase 1, Summer 2026
Last completed: Phase 1 Project - Robot class + mission loop
Next: Phase 1 Project - obstacle check + file logging inside the loop


## Files in repo
exercises/robot_pose.py
exercises/robot_functions.py
exercises/robot_loops.py
exercises/terminal-practice.md
notes/math/ — Lessons 1-6
notes/Python/ — Lessons 8-10
notes/tools/ — Lesson 7

## Key concepts mastered
- Robot pose (x, y, θ)
- Trig: Δx = d×cos(θ), Δy = d×sin(θ)
- Vectors, magnitude: |v| = √(vx²+vy²)
- atan2(Δy, Δx) for direction
- Rotation matrix R(θ) = [cos,-sin; sin,cos]
- Terminal navigation: pwd, ls, cd
- Git workflow: add, commit, push, pull
- Python: variables, types, import math
- Functions: def, parameters, return
- Conditionals: if/elif/else
- Loops: for with range(), while with condition
- Overshoot: smaller steps = more precision

## Personality and learning notes
- Gets nervous and doubts himself frequently
- Needs reassurance connected to specific evidence
- Fear of not coding from scratch
- Responds well to honest direct feedback
- Never quits mid-session
- Two semesters left before graduation
- Goal: NVIDIA, Boston Dynamics, own robotics company
- Also targeting MIT/Harvard/CMU for Masters

## Git workflow reminder
cd ~/Documents/robotics-mastery
git add .
git commit -m "message"
git push
(if rejected: git pull first)
(if Vim opens: Escape then :wq then Enter)

## Common errors to watch for
- math.radiants (typo) → math.radians
- Saving files outside robotics-mastery folder
- Pasting multiple commands at once in terminal
- Mixing navigation commands with git commands
- (-n)² = positive, never negative
