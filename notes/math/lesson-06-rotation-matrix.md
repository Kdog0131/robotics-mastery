What the rotation matrix structure is (the 2×2 template): The structure is always two rows and two columns.

The two-step process: 

R(θ) = [cos(θ)   -sin(θ)]
        [sin(θ)    cos(θ)]

Top-left:     cos    Top-right:    -sin  (minus sign)
Bottom-left:  sin    Bottom-right:  cos


STEP 1: Substitute the angle → get a plain number matrix

R(45°) = [cos(45°)  -sin(45°)]  =  [0.707  -0.707]
          [sin(45°)   cos(45°)]     [0.707   0.707]

STEP 2: Multiply as plain numbers

[0.707  -0.707] [3]   =  [0.707×3 + (-0.707)×0]   =  [2.121]
[0.707   0.707] [0]      [0.707×3 +   0.707×0  ]      [2.121]


What R(90°) × [0,1] gives and why it's west not east: Since the rotation matrix always rotates counterclockwise, the direction will be west.

R(90°) × [0, 1] = [-1, 0]  →  pointing west

Row 1: 0×0 + (−1)×1 = −1
Row 2: 1×0 +   0×1 =  0



What you got wrong and fixed: WHen doing the roation matrix calculations I would repeatedly mix up the the order of [cos  -sin] and [sin cos], but after some practice I improved.
