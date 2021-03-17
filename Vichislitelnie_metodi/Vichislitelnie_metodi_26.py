import numpy as np
import math
import matplotlib.pyplot as plt

a = 0.0
b = 2.0
#h = 0.2
h = (b - a) / 10
eps = 10 ** (-6)

f = []

def erf(x):
    Sn = 0
    n = 0
    while(True):
        an = ((x ** (2 * n + 1)) / (math.factorial(n) * (2 * n + 1)))
        if (an <= eps):
            break
        Sn += ((-1) ** n) * an
        n += 1
    Sn *= 2 / np.sqrt(np.pi)
    return Sn

def result1(func, step):
    xi = a
    while(xi <= b + eps):
        res = erf(xi)
        func.append([xi, res])
        xi += step

result1(f, h)

def product_series_numerator(x, k, j, func):
    product = 1
    for i in range(len(func)):
        if (func[i][0] != func[k][0] and func[i][0] != func[j][0]):
            product *= (x - func[i][0])
    return product

def product_series_denominator(xk, k, func):
    product = 1
    for i in range(len(func)):
        if func[i][0] != func[k][0]:
            product *= (xk - func[i][0])
    return product

def l(x, k, func):
    sum = 0
    for j in range(len(func)):
        if (func[j][0] != func[k][0]):
            sum += product_series_numerator(x, k, j, func) / product_series_denominator(func[k][0], k, func)
    return sum

def result2(func, x):
    res = []
    for i in x:
        sum = 0
        row = []
        for k in range(len(func)):
            sum += func[k][1] * l(i, k, func)
        row.append(i)
        row.append(sum)
        help = (2 / np.sqrt(np.pi)) * np.exp((-1) * i ** 2)
        row.append(help)
        row.append(sum - help)
        res.append(row)
    return res

x = []
step = 0
for i in range(200):
    res = step
    x.append(res)
    step += 0.01

res2 = result2(f, x)
for i in res2:
    print(i)
plt.title(str(h))
row0 = []
row1 = []
for i in res2:
    row0.append(i[0])
    row1.append(i[1] - i[2])
plt.plot(row0, row1)
plt.show()
#проверить между узлами