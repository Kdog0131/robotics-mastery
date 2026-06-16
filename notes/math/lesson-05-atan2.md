The three-step algorithim: 

The arctan failiure and why atan2 fixeses it: arctan shares the same information with delta x and delta y since it uses thier ratio. atan2 looks at delta x and delta y individually to get the proper angle.

+y (north)
          |
Q2        |        Q1
northwest |  northeast
  Δx<0   |   Δx>0
  Δy>0   |   Δy>0
          |
──────────┼──────────  +x (east)
          |
  Δx<0   |   Δx>0
  Δy<0   |   Δy<0
Q3        |        Q4
southwest |  southeast
          |
          -y (south)

The parenteses rule: Always write (delta x)^2, not - deltax^2.

What I got wrong and fixed: I struggled heavily with trying to calculate delta x and delta y individually aswell as   
