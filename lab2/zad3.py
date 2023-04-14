import matplotlib.pyplot as plt
import numpy as np


a = float(input())
b = float(input())
c = float(input())
d = float(input())


def func(x):
    return a*(x**3) + b*(x**2) + c*x + d


x = [i for i in range(0, 100)]
y = [func(i) for i in range(0, 100)]
fig, axs = plt.subplots(2)
fig.suptitle('Два графика')
axs[0].plot(x, y)

x1 = []
y1 = []
for theta in range(0, 31):
    r = ((theta)**2)
    x1.append(r*np.cos(theta))
    y1.append(r*np.sin(theta))
axs[1].plot(x1, y1)

coeff = [a, b, c, d]
print(np.roots(coeff))

plt.show()
