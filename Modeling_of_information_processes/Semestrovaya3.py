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
    x_i = round(rn.uniform(-r, r), 1)
    y_help = np.sqrt((r + x_i) * (r - x_i))
    y_i = round(rn.uniform(-y_help, y_help), 1)
    print(f'{i} ({x_i}, {y_i})')
    x.append(x_i)
    y.append(y_i)

a = []
for i in range(2, n + 1):
    a_i = round((3 / 2) * np.abs(np.sin(i)), 2)
    print(f'a({i}) = {a_i}')
    a.append(a_i)

c = []

for i in range(n):
    c_i = []
    for j in range(n):
        res = round(np.sqrt(np.square(x[i] - x[j]) + np.square(y[i] - y[j])), 2)
        c_i.append(res)
    c.append(c_i)

for i in c:
    print(i)

array_x_y = np.vstack((x, y))

df = pd.DataFrame(array_x_y)
df.to_excel('./array_X_Y3.xlsx')

df = pd.DataFrame(a)
df.to_excel('./a3.xlsx')

df = pd.DataFrame(c)
df.to_excel('./с3.xlsx')

t = np.arange(0, 2*np.pi, 0.01)          # угол t от 0 до 2pi с шагом 0.01
r = 20                                    # радиус 4

plt.plot(r*np.sin(t), r*np.cos(t), lw=3) # x и у задаем как numpy функции от t
plt.axis('equal')                        # масштаб осей Х и У одинаковый (чтобы круг не был овалом)
plt.scatter(0, 0)
plt.scatter(x, y)
plt.show()