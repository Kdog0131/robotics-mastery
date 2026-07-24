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
Pillar 1, Math for Robotics — Summer 2026 (continuing)

Covered previously (June 2026), needs review: Robot pose, trigonometry 
(sin/cos movement), vectors + magnitude, atan2 for direction, 
2D rotation matrices — NOT confirmed mastered, hasn't been reviewed 
in several weeks

Last completed (most recent session): Quick trigonometry refresher — 
single-angle cos/sin robot movement calculation in trig_movement.py

Next: Review and rebuild vectors, atan2, and rotation matrices from 
the ground up before moving forward in Pillar 1

Completed Projects: 
- Phase 1 (Python Robot Sensor Simulator) — complete, documented, LinkedIn posted
- Phase 2 (Multi-Robot Fleet Monitor) — complete, documented, LinkedIn posted

Foundation complete: Python fundamentals through classes, file I/O, 
error handling, sets/tuples, git branching

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
