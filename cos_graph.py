#cos graph

import numpy as np
import matplotlib.pyplot as plt

#We start at zero, stop at 4π and step by 0.1 radians
x = np.arange(0,4*np.pi,0.1)
y = np.sin(x)
plt.plot(x,y)
plt.show()