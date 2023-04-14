import numpy as np
import matplotlib.pyplot as plt

plt.axes(projection='polar')

a = 4

rads = np.arange(0, (2 * np.pi), 0.01)

for rad in rads:
    r = a + (a*np.cos(rad))
    plt.polar(rad, r, 'g.')

plt.show()
