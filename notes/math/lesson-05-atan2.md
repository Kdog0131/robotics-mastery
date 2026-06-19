The three-step algorithim: First you solve for delta x and delta y, then you use the magnitude formula to get the distance of how far the robot traveled. 



Step 1: Find delta x and delta y (Subtracting X_final - X_inital and Y_final - Y_inital)
Step 2: Find distance → |v| = √(Δx² + Δy²)
Step 3: Find angle → θ = atan2(Δy, Δx)



These are TWO separate outputs. Magnitude ≠ angle.


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



Key Rule: atan2(delta y, delta x), Delta y comes first, Delta x comes second



What I got wrong and fixed: I struggled heavily with trying to calculate delta x and delta y individually aswell as just doing the steps wrong in general. After learning the technique of subtracting the x_final,x_inital and y_final,y_inital I was able to successfully solve those kinds of problems. 
