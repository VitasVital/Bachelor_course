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

def result1(resf):
    xi = a
    while(xi <= b):
        res = erf(xi)
        resf.append([xi, res])
        xi += h
    return resf

result1(f)

for i in f:
    print(i)

def product_series():
    return

def l(x):
    return


def result2(resf):
    xi = a
    Lx = 0
    for k in resf:
        print(k[0], ' ', k[1])
        Lx += k[1] * l(k[0])