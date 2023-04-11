import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D


#График функции двух переменных с не единственным экстремумом
x = np.arange(-2,2,0.1)
y = np.arange(-2,2,0.1)
x,y = np.meshgrid(x,y)

def f(x, y):
    return (1 - y**5 + x**5)*np.exp(-x**2-y**2)

fig1 = plt.figure()
ax1 = plt.axes(projection ='3d')
ax1.plot_surface(x, y, f(x, y), rstride=1, cstride=1, cmap = 'inferno')
ax1.set_title('3D surface')


#Контурная диаграмма
fig2 = plt.figure()
C = plt.contour(x ,y ,f(x,y),10,colors='black')
plt.contourf(x ,y, f(x,y), 10, cmap = 'inferno')
plt.clabel(C, inline=1, fontsize=10)
plt.colorbar()


#Пространственная кривая
z1 = np.linspace(0, 1, 100)
x1 = z1 * np.sin(25 * z1)
y1 = z1 * np.cos(25 * z1)

fig3 = plt.figure()
ax2 = plt.axes(projection ='3d')
ax2.plot3D(x1, y1, z1, 'green')
ax2.set_title('3D line')




plt.show()