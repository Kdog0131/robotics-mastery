What the rotation matrix structure is (the 2×2 template): The structure is always two rows and two columns.

The two-step process: 

STEP 1: Substitute the angle → get a plain number matrix

R(45°) = [cos(45°)  -sin(45°)]  =  [0.707  -0.707]
          [sin(45°)   cos(45°)]     [0.707   0.707]

STEP 2: Multiply as plain numbers

[0.707  -0.707] [3]   =  [0.707×3 + (-0.707)×0]   =  [2.121]
[0.707   0.707] [0]      [0.707×3 +   0.707×0  ]      [2.121]

What R(90°) × [0,1] gives and why it's west not east: Since the rotation matrix always rotates counterclockwise, the direction will be west.
What you got wrong and fixed: 
