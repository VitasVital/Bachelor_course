import numpy as np
from scipy.optimize import linprog
from copy import copy

f1 = open('a_l_read.txt', 'r')
f2 = open('b_l_read.txt', 'r')
f3 = open('c_read.txt', 'r')
a_l1 = []
a_l1_copy = [line.split() for line in f1]
b_l1 = f2.readline().split()
c1 = f3.readline().split()

#два положительных в иксе

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

print('-------------------------------------------------------------------------\nСвоё решение\n')

def find_basis(a):
    ind = []
    for i in range(len(a)):
        for j in range(len(a[i])):
            if (a[i][j] == 1):
                sum = a.T[j] @ np.ones(len(a))
                if (sum == 1):
                    ind.append([i, j])
                    break
    return ind

def enter_additional_variables(a, basis):
    add_column = []
    for i in range(len(a)):
        finded = False
        for j in basis:
            if (j[0] == i):
                finded = True
                break
        if (finded == False):
            add_column.append(i)
    for i in add_column:
        column = np.zeros(len(a))
        column[i] += 1
        a = np.column_stack((a, column))
    return a

def Simplex(a, b, c):
    basis = find_basis(a)
    print(basis)
    if (len(basis) < len(a)):
        a = enter_additional_variables(a, basis)
    print(a)
    return

Simplex(np.array(a_l1), np.array(b_l1), np.array(c_new1))

f1.close()
f2.close()
f3.close()