import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from mpl_toolkits.mplot3d import Axes3D as ax

x = np.outer(np.linspace(-10, 10, 100), np.ones(100))
y = x.copy().T
z = y**3 + x**3 - x*y + 8*x**2
fig = plt.figure()
ax = plt.axes(projection ='3d')
ax.plot_surface(x, y, z, edgecolor ='green')
plt.show()