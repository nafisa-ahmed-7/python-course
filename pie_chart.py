#pie chart

import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15,5])
names = ["Apples","Bananas","Cherries","Coconuts","Guavas"]
fruit_col=["red", "hotpink", "b", "#4CAF50","grey"]
plt.title("Pie Chart of fruit consumption")

plt.pie(y,labels=names,colors=fruit_col,autopct='%1.0f%%')
plt.legend(title="Fruits data",bbox_to_anchor=(1,0),bbox_transform=plt.gcf().transFigure,loc="lower right")
plt.show()