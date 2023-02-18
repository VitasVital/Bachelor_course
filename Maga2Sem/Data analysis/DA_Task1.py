import numpy as np
import matplotlib.pyplot as plt
import math
from numpy.random import uniform

def normal_distribution(input_x, input_mu, input_var):
    return np.exp(-((input_x - input_mu) ** 2) / (2 * input_var ** 2)) / np.sqrt(2 * np.pi * input_var ** 2)

def student(input_x, input_mu, input_var, input_nu):
    res1 = math.gamma((input_nu + 1) / 2)
    res2 = (1 + ((input_x - input_mu) ** 2) / (input_nu * input_var ** 2)) ** (-(input_nu + 1) / 2)
    res3 = np.sqrt(input_nu * np.pi) * math.gamma(input_nu / 2)
    return (res1 * res2) / res3

def laplace(input_x, input_mu, input_var):
    b = np.sqrt(input_var / 2)
    return np.exp(-np.abs(input_x - input_mu) / b) / (2 * b)

def task1():
    mu = 0
    var = 3
    nu = 1
    x = np.linspace(-10, 10, 1000)
    y_normal = normal_distribution(x, mu, var)
    y_student = student(x, mu, var, nu)
    y_laplace = laplace(x, mu, var)

    plt.step(x, y_normal)
    plt.step(x, y_student)
    plt.step(x, y_laplace)

    plt.show()

def task2():
    res1 = uniform(0, 1, (1000, 10000))
    print(res1)
    res = np.mean(res1)
    print(res)
    return

# task1()
task2()