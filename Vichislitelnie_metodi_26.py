import numpy as np
import math

a = 0.0
b = 2.0
h = 0.2
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

def result1():
    xi = a
    while(xi <= b):
        res = erf(xi)
        f.append([xi, res])
        xi += h

result1()

print("\n1 result\n")
for i in f:
    print(i)

def product_series_numerator(x, k, j):
    product = 1
    for i in range(len(f)):
        if (f[i][0] != f[k][0] and f[i][0] != f[j][0]):
            product *= (x - f[i][0])
    return product

def product_series_denominator(xk, k):
    product = 1
    for i in range(len(f)):
        if f[i][0] != f[k][0]:
            product *= (xk - f[i][0])
    return product

def l(x, k):
    sum = 0
    for j in range(len(f)):
        if (f[j][0] != f[k][0]):
            sum += product_series_numerator(x, k, j) / product_series_denominator(f[k][0], k)
    return sum

def result2(x):
    sum = 0
    for k in range(len(f)):
        sum += f[k][1] * l(x, k)
    return sum

print("\n2 result\n")
for i in range(len(f)):
    print(f[i][0], ' ', result2(f[i][0]), ' ', (2 / np.sqrt(np.pi)) * np.exp((-1) * f[i][0] ** 2))