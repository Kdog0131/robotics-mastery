What sin and cos are: sin(theta) is the fraction of movement that goes into y, how much of d becomes delta y. cos(theta) is the fraction of movement that goes into x - houw much distance becomes delta x. Essentially sin and cos tell you how much x and y change as you move.

● ← end position (where the robot ends up)
                 /|
                / |
               /  |
        d     /   |  Δy
    (distance)/   |  (how much y changed)
             /    |
            /     |
           /  θ   |
          ●───────●
     start       └─ right angle (90°)
        (0,0)
              Δx
        (how much x changed)



┌────────┬──────────┬──────────┬──────────────────────────┐
│   θ    │  cos(θ)  │  sin(θ)  │  What it means           │
├────────┼──────────┼──────────┼──────────────────────────┤
│   0°   │  1.000   │  0.000   │ all movement → x only    │
│  30°   │  0.866   │  0.500   │ mostly x, some y         │
│  45°   │  0.707   │  0.707   │ equal split: x = y       │
│  60°   │  0.500   │  0.866   │ some x, mostly y         │
│  90°   │  0.000   │  1.000   │ all movement → y only    │
└────────┴──────────┴──────────┴──────────────────────────┘


┌──────────────────────────────────┐
│  Δx = d × cos(θ)                 │
│  Δy = d × sin(θ)                 │
└──────────────────────────────────┘

THE √n/2 PATTERN

sin(0°)  = √0/2 = 0/2     = 0.000
sin(30°) = √1/2 = 1/2     = 0.500
sin(45°) = √2/2           = 0.707
sin(60°) = √3/2           = 0.866
sin(90°) = √4/2 = 2/2     = 1.000

For cos — it's the exact reverse:
cos(0°) = 1.000,  cos(30°) = 0.866,  cos(45°) = 0.707
cos(60°) = 0.500, cos(90°) = 0.000


The two key formulas: delta x = d x cos(theta), delta y = d x sin(theta).

What I got wrong and fixed: I was confused on how event though there may be no horizontal movement, there can be vertical movement that can still occur. 
