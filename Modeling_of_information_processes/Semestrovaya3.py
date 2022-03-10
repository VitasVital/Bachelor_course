import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import linprog
import pandas as pd
import random as rn

n = 10
k = 6
r = 20

x = []
y = []
for i in range(1, n + 1):
    x_i = rn.uniform(-r, r)
    y_help = np.sqrt((r + x_i) * (r - x_i))
    y_i = rn.uniform(-y_help, y_help)
    print(f'x({i}) = {x_i} y({i}) = {y_i}')
    x.append(round(x_i, 3))
    y.append(round(y_i, 3))

a = []
for i in range(1, n + 1):
    a_i = (3 / 2) * np.abs(np.sin(i))
    print(f'a({i}) = {a_i}')
    a.append(round(a_i, 3))

t = np.arange(0, 2*np.pi, 0.01)          # угол t от 0 до 2pi с шагом 0.01
r = 20                                    # радиус 4

plt.plot(r*np.sin(t), r*np.cos(t), lw=3) # x и у задаем как numpy функции от t
plt.axis('equal')                        # масштаб осей Х и У одинаковый (чтобы круг не был овалом)
plt.scatter(0, 0)
plt.scatter(x, y)
plt.show()