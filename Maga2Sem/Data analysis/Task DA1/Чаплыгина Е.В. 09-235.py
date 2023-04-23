import numpy as np
import matplotlib.pyplot as plt
import math
from numpy.random import uniform

def gaussian(x, mu, var):
    return np.exp(-((x - mu) ** 2) / (2 * var ** 2)) / np.sqrt(2 * np.pi * var ** 2)

def student(x, mu, var, nu):
    res1 = math.gamma((nu + 1) / 2)
    res2 = (1 + ((x - mu) ** 2) / (nu * var ** 2)) ** (-(nu + 1) / 2)
    res3 = np.sqrt(nu * np.pi) * math.gamma(nu / 2)
    return (res1 * res2) / res3

def laplacian(x, mu, var):
    b = np.sqrt(var / 2)
    return np.exp(-np.abs(x - mu) / b) / (2 * b)

def IG(x, a, b):
    return (b ** a * x ** (-(a + 1)) * np.exp(-b / x)) / math.gamma(a)

def DA1():
    mu = 0
    var = 2
    nu = 1
    x = np.linspace(-5, 5, 1000)
    y_normal = gaussian(x, mu, var)
    y_student = student(x, mu, var, nu)
    y_laplace = laplacian(x, mu, var)
    plt.title('Task 1')
    plt.step(x, y_normal, label='Gaussian')
    plt.step(x, y_student, label='Student')
    plt.step(x, y_laplace, label='Laplacian')
    plt.legend()
    plt.show()
    return

def DA2():
    x = np.linspace(0.43, 0.57, 1000)
    y = np.mean(uniform(0, 1, (1000, 10000)), axis=0)
    average_y = np.mean(y)
    var_y = np.sqrt(np.var(y))
    y_normal = gaussian(x, average_y, var_y)
    plt.title('Task 2')
    plt.hist(y, bins=100, density=True)
    plt.step(x, y_normal)
    plt.show()
    return

def DA3():
    x = np.linspace(0.1, 20, 10000)
    a = 2
    b = 2
    Y = 1 / np.random.gamma(a, 1 / b, 1000)
    ig = IG(x, a, b)
    plt.title('Task 3')
    plt.hist(Y, bins=100, label='Y histogram', density=True)
    plt.step(x, ig, label='IG')
    plt.legend()
    plt.show()
    return

DA1()
DA2()
DA3()
