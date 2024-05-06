#pip install scipy
#pip install matplotlib
#pip install numpy


import numpy as np
import matplotlib.pyplot as plt


def expression(x, y):
    return 1.2 + (np.sqrt(1 - (np.sqrt(x**2 + y**2))**2) + 1 - x**2 - y**2) * (np.sin(10 * (x * 3 + y / 5 + 7)) + 1 / 4)


x = np.linspace(-1.6, 1.6, 100)
y = np.linspace(-1.6, 1.6, 100)
X, Y = np.meshgrid(x, y)


Z = expression(X, Y)


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Expression Value')

plt.show()