#plot y=x**2

import matplotlib.pyplot as plt
x= range(-50,50)
y= [x*x for x in x]
plt.title("Graph of function y=x**2")
plt.xlabel("X Axis Label")
plt.ylabel("Y Axis Label")
plt.plot(x,y,'red',)
plt.plot(x,y,'')
plt.show()