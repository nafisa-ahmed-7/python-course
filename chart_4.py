
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
# syntax for 3-D projection
ax = plt.axes(projection='3d')
# defining all 3 axes
z = np.linspace(0, 1, 100)
x = z**2
y = z**3
# plotting
ax.plot3D(x, y, z, 'r')
ax.set_title('3D line graph plotting')
plt.show()