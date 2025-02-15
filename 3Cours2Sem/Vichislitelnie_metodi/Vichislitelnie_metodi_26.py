import numpy as np
import math
import matplotlib.pyplot as plt
import pandas as pd

a = 0.0
b = 2.0
h = (b - a) / 10
eps = 10 ** (-6)

f = []

def erf(x):
    Sn = 0
    n = 0
    while(True):
        an = ((x ** (2 * n + 1)) / (math.factorial(n) * (2 * n + 1)))
        if (abs(an) <= eps):
            break
        Sn += ((-1) ** n) * an
        n += 1
    Sn *= 2 / np.sqrt(np.pi)
    return Sn

def result1(func, step):
    xi = a
    while(xi <= b):
        res = erf(xi)
        func.append([xi, res])
        xi += step
    df = pd.DataFrame(func)
    df.to_excel('./res1.xlsx')
    plt.figure()
    plt.title('График erf(x).\n Шаг = ' + str(step))
    plt.plot(np.array(func).T[0], np.array(func).T[1])
    for i, txt in enumerate(np.array(func).T[1]):
        plt.annotate(np.array(func).T[1, i], (np.array(func).T[0, i], np.array(func).T[1, i]))
    plt.show()

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

def make_test(x, res2):
    function1 = []
    for i in x:
        res = (2 / np.sqrt(np.pi)) * np.exp(-1 * i ** 2)
        function1.append(res)
    step = 2.0 / len(x)

    row0 = []
    row1 = []
    for i in res2:
        row0.append(i[0])
        row1.append(i[1])

    fig = plt.figure()
    ax = fig.add_subplot(111, label="1")
    ax2 = fig.add_subplot(111, label="2", frame_on=False)
    plt.title('erf(x) по Тейлору')

    ax.plot(x, function1, color="C0", label = ['Запрограммированный'])
    ax.set_xlabel("x label 1", color="C0")
    ax.set_ylabel("y label 1" + str(step), color="C0")
    ax.tick_params(axis='x', colors="C0")
    ax.tick_params(axis='y', colors="C0")
    ax.legend(loc=(0.0, 0.1))

    ax2.scatter(row0, row1, color="C1", label = ['Встроенный'])
    ax2.xaxis.tick_top()
    ax2.yaxis.tick_right()
    ax2.set_xlabel('x label 2. Шаг разбиения = ' + str(step), color="C1")
    ax2.set_ylabel('y label 2', color="C1")
    ax2.xaxis.set_label_position('top')
    ax2.yaxis.set_label_position('right')
    ax2.tick_params(axis='x', colors="C1")
    ax2.tick_params(axis='y', colors="C1")
    ax2.legend(loc=(0.0, 0.2))
    for i, txt in enumerate(row1):
        ax2.annotate(row1[i], (x[i], row1[i]))

    row_razn0 = []
    row_razn1 = []
    for i in res2:
        row_razn0.append(i[0])
        row_razn1.append(i[3])
    plt.figure()
    plt.title('График погрешности для равномерно распределенных узлов.\n Шаг h = ' + str(step))
    plt.plot(row_razn0, row_razn1)
    plt.show()
    return

def more_tests():
    x = np.linspace(0, 2, 20)
    res2 = result2(f, x)
    for j in res2:
        print(j)
    df = pd.DataFrame(res2)
    df.to_excel('./res2.xlsx')
    make_test(x, res2)
    return

more_tests()

c = 0.0
d = 2.0
eps_1 = 10 ** (-4)

def fi(t):
    res = (2 / np.sqrt(np.pi)) * np.exp((-1) * t ** 2)
    return res

def S(z, hN):
    res = (hN / 2) * (fi(z + (hN / 2) * (1 - 1 / np.sqrt(3))) + fi(z + (hN / 2) * (1 + 1 / np.sqrt(3))))
    return res

def result3(x):
    S_res = []
    for _x in range(1, len(x)):
        N = 1
        hN = (x[_x] - x[_x - 1]) / N
        N_2 = N * 2
        hN_2 = (x[_x] - x[_x - 1]) / N_2
        flag = True
        while (flag):
            S_res_N = 0
            for i in range(N):
                zi = c + i * hN
                S_res_N += S(zi, hN)
            S_res_2N = 0
            for i in range(N_2):
                zi = c + i * hN_2
                S_res_2N += S(zi, hN_2)
            if (abs(S_res_N - S_res_2N) <= eps_1):
                S_res.append([x[_x], S_res_N])
                flag = False
            else:
                N += 1
                hN = (x[_x] - x[_x - 1]) / N
                N_2 = N * 2
                hN_2 = (x[_x] - x[_x - 1]) / N_2
                # print('S_res_N = ', S_res_N)
                # print('S_res_2N = ', S_res_2N)
    return S_res

res3 = result3(np.array(f).T[0])
print(res3)
df = pd.DataFrame(res3)
df.to_excel('./res3.xlsx')

x = np.linspace(0, 2, len(res3))
plt.figure()
plt.plot(x, res3)
plt.show()