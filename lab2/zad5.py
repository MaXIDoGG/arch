import matplotlib.pyplot as plt
import sympy as sp


x = sp.Symbol('x')
y = 'sin(x^2) - cos(4*x^5) + x^6 - log(x^10)'

ydif = sp.diff(y)
yinteg = sp.integrate(y)

ydif = str(sp.simplify(ydif))
yinteg = str(sp.simplify(ydif))

ydif = ydif.replace('**', '^')
yinteg = yinteg.replace('**', '^')

print(ydif)
print(yinteg)

# Изображение формулы

fig = plt.figure()
fig.text(100, 350, ydif, color="black", fontsize=11)
plt.savefig(dpi=200, fname = 'text.png', format="png", bbox_inches="tight",
                    pad_inches=0)