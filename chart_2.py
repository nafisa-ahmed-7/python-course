#sin graph

import numpy as np
import matplotlib.pyplot as plot

# Get x values of the sine wave i.e. start,step,stop
x = np.arange(0, 10, 0.1);
y = np.sin(x)
plot.plot(x,y)
# Give a title for the sine wave plot
plot.title('Sine wave')
plot.show()