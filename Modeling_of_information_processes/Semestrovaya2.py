import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import linprog
import pandas as pd
import random as rn

n = 10
k = 6
r = 20

tau = []

for i in range(1, n + 1):
    tau_i = 5 + 4 * np.sin(k * i / 2)
    print(f'tau({i}) = {tau_i}')
    tau.append(round(tau_i, 3))

x = []
y = []
for i in range(1, n + 1):
    x_i = rn.uniform(-r, r)
    y_i = np.sqrt((r + x_i) * (r - x_i)) * rn.choice([-1, 1])
    print(f'x({i}) = {x_i} y({i}) = {y_i}')
    x.append(round(x_i, 3))
    y.append(round(y_i, 3))

array_x_y = np.vstack((x, y))
print(array_x_y)

x_main = round((np.array(tau) @ np.array(x).T) / (np.array(tau) @ np.ones(n)), 3)
y_main = round((np.array(tau) @ np.array(y).T) / (np.array(tau) @ np.ones(n)), 3)
print(f'x* = {x_main} y* = {y_main}')

t = np.arange(0, 2*np.pi, 0.01)          # угол t от 0 до 2pi с шагом 0.01
r = 20                                    # радиус 4

plt.plot(r*np.sin(t), r*np.cos(t), lw=3) # x и у задаем как numpy функции от t
plt.axis('equal')                        # масштаб осей Х и У одинаковый (чтобы круг не был овалом)
plt.scatter(0, 0)
plt.scatter(x, y)
plt.scatter(x_main, y_main)
plt.show()

df = pd.DataFrame(tau)
df.to_excel('./tau2.xlsx')

df = pd.DataFrame(array_x_y)
df.to_excel('./array_X_Y2.xlsx')

df = pd.DataFrame([x_main, y_main])
df.to_excel('./array_X_Y_result2.xlsx')