import numpy as np
import matplotlib.pyplot as plt

"""
    NumPy program to compute the x and y coordinates for points on a sine curve and plot the points using matplotlib
"""

x = np.arange(0, 7, 0.1)
y = np.sin(x)
plt.plot(x, y)
plt.show()