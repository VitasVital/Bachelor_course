import numpy as np
from scipy.optimize import linprog

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