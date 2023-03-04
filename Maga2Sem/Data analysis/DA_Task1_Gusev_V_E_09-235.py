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

def Ga(input_x, a, b):
    return (b ** a * input_x ** (a - 1) * np.exp(-input_x * b)) / math.gamma(a)

def IG(input_x, a, b):
    return (b ** a * input_x ** (-(a + 1)) * np.exp(-b / input_x)) / math.gamma(a)

def task1():
    mu = 0
    var = 3
    nu = 1
    x = np.linspace(-10, 10, 1000)
    y_normal = normal_distribution(x, mu, var)
    y_student = student(x, mu, var, nu)
    y_laplace = laplace(x, mu, var)

    plt.title('Задание 1')
    plt.step(x, y_normal, label='Нормальное')
    plt.step(x, y_student, label='Стьюдент')
    plt.step(x, y_laplace, label='Лаплас')
    plt.legend()

    plt.show()
    return

def task2():
    x = np.linspace(0.46, 0.54, 1000)
    y = np.mean(uniform(0, 1, (1000, 10000)), axis=0)
    average_y = np.mean(y)
    var_y = np.sqrt(np.var(y))
    y_normal = normal_distribution(x, average_y, var_y)

    plt.title('Задание 2')
    plt.hist(y, bins=100, density=True)
    plt.step(x, y_normal)
    plt.show()
    return

def task3():
    x = np.linspace(0.1, 20, 10000)
    a = 2
    b = 2

    Y = 1 / np.random.gamma(a, 1 / b, 1000)
    ig = IG(x, a, b)

    plt.title('Задание 3')
    plt.hist(Y, bins=100, label='Y гистограмма', density=True)
    plt.step(x, ig, label='IG')
    plt.legend()
    plt.show()
    return

task1()
task2()
task3()
