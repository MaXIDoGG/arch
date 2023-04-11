import numpy as np
import sympy as sp

x = sp.Symbol('x')
y = input()

ydif = sp.diff(y)
yinteg = sp.integrate(y)

print(ydif, '   ', yinteg)
