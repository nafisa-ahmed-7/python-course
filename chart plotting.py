import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,10)
y = x ^ 2

x1 = np.arange(3,7)
y1 = x1**2

#Label the axes
plt.title("Example of Line graph")
plt.xlabel("X Axis Label")
plt.ylabel("Y Axis Label")

#Draw the data
plt.plot(x,y, 'go-', color='red' )
#plt.plot(x,y, '>')

#Annotate specific points
plt.annotate(xy=[5,2], text="Point one")

#draw a second series
plt.plot(x1,y1, 'b<--')

#Ticks
#xticks, yticks, major locator, linear locator
#Legend
plt.legend(['series one','series two'], loc=1)

plt.show()

#link : https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html
'''
y=x**2 , sin, cos, 3-D graph (x,y,z)
pie-chart, line graph, bar diagram(histogram), scatter plot
'''
#saving
#plt.savefig('graph_1.png', format='png')