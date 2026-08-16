import matplotlib.pyplot as plt #Here I imported matplotlib.pylot as plit so that this program can graph coordinates.

x_values = [0, 3, 5] #Here I made a x_values variable and I have it store a list with the numbers 0, 3 and 5.
y_values = [0, 4, 1] #Here I made a y_values variable and I have it store a list with the numbers 0, 4 and 1.

plt.plot(x_values, y_values, 'o-') #Here I have matplotlib use its plot function to plot x_values as x using the numbers in the list the x_values variable is holding, and y_values as y using the numbers the y_values list is holding, with 'o-' so that it draws a circle connecting those coordinates which makes a path.
plt.show() #Here I have matplotlib use it show function to show the results of its graphing.

