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

def enter_additional_variables(a, c, basis):
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
        basis.append([i, len(a[0])])
        a = np.column_stack((a, column))
        c = np.append(c, 0)
    return a, c, basis

#Оптимальность. Все дельта должны быть отрицательными
def check_optimality(delta):
    for i in delta:
        if i > 0:
            return False
    return True

#Допустимость. Все b (А0) должны быть неотрицательными
def check_validity(b):
    for i in b:
        if i < 0:
            return False
    return True

def calculate_delta():
    return

def iteration(a, b, c, basis):
    A0 = b
    C = []
    basis.sort(key = lambda basis: basis[0])
    for i in basis:
        C.append(c[i[1]])
    print(C)
    return

def Simplex(a, b, c):
    added_basis = find_basis(a)
    if (len(added_basis) < len(a)):
        a, c, basis = enter_additional_variables(a, c, added_basis)
    print(a)
    print(basis)
    print(c)
    iteration(a, b, c, basis)
    return

Simplex(np.array(a_l1), np.array(b_l1), np.array(c_new1))

f1.close()
f2.close()
f3.close()