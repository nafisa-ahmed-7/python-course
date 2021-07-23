#pie chart

import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15,5])
names = ["Apples","Bananas","Cherries","Coconuts","Guavas"]
fruit_col=["black", "hotpink", "b", "#4CAF50","grey"]
plt.title("Pie Chart of fruit consumption")

plt.pie(y,labels=names,colors=fruit_col)
plt.legend(title="Fruits data")
plt.show()