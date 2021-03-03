import numpy as np
from scipy.optimize import linprog
import time

m = 3
n = 3
c = [3, 6, 5, 4, 9, 2, 3, 6, 2]
a = [58, 60, 40]
b = [30, 50, 20]
start = time.time()

A_1 = [[1, 1, 1, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 1, 1, 1, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 1, 1, 1]]
b_1 = a
A_2 = [[1, 0, 0, 1, 0, 0, 1, 0, 0],
       [0, 1, 0, 0, 1, 0, 0, 1, 0],
       [0, 0, 1, 0, 0, 1, 0, 0, 1]]
b_2 = b
res = linprog(c, A_1, b_1, A_2, b_2)
P = np.dot(res.x, c)
P1 = np.dot(c, res.x)
stop = time.time()
print("Time:", stop-start)

print(res)
print("Check of sum", P, P1)

print("-----------------------------------------------------------")

n = 5
m = 3
a_l = [[55, 69, 77, 58, 93],
       [87, 99, 60, 85, 76],
       [94, 56, 86, 55, 64]]
b_l = [2211, 4836, 3712]
c = [74, 99, 91, 87, 95]
c_new = np.dot(c, -1)

res_lin = linprog(c_new, a_l, b_l)
print(res_lin)
print(np.dot(res_lin.fun, -1))

print("--------------------------------------------------------------------")
print("Считывание из файла")

n = 5
m = 3
f1 = open('a_l_read.txt', 'r')
f2 = open('b_l_read.txt', 'r')
f3 = open('c_read.txt', 'r')
a_l1 = []
a_l1_copy = [line.split() for line in f1]
b_l1 = f2.readline().split()
c1 = f3.readline().split()

for i in a_l1_copy:
    array = []
    for j in i:
        array.append(float(j))
    a_l1.append(array)
b_l1 = [float(elem) for elem in b_l1]
c1 = [float(elem) for elem in c1]
c_new1 = np.dot(c1, -1)

res_lin1 = linprog(c_new1, a_l1, b_l1)
print(res_lin1)
print(np.dot(res_lin1.fun, -1))

f1.close()
f2.close()
f3.close()