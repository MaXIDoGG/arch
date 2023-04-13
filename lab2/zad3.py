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
plt.plot(x, y)

coeff = [a, b, c, d]
print(np.roots(coeff))

plt.show()
