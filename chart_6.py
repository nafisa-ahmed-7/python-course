#line graph

import matplotlib.pyplot as plt

#line 1 points
x1 = [1, 2, 3]
y1 = [2, 4, 1]
plt.plot(x1, y1, label="line 1")
#line 2 points
x2 = [1, 2, 3]
y2 = [4, 1, 3]
plt.plot(x2, y2, label="line 2")
#naming the x and y axis
plt.xlabel('x - axis')
plt.ylabel('y - axis')
#graph title
plt.title('Two lines graph')
# show a legend on the plot
plt.legend()
plt.show()