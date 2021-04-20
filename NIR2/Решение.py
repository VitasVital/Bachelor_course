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

def calculate_delta(a, c, C):
    delta = []
    for _c in range(len(c)):
        res = a.T[_c] @ C - c[_c]
        delta.append(res)
    return np.array(delta)

def find_k(delta):
    res = 1
    for i in range(2, len(delta)):
        if (delta[i] > delta[res]):
            res = i
    return res

def step3(ak):
    res = 0
    for i in range(len(ak)):
        if (ak[i] > ak[res]):
            res = i
    return res

def step4(A0, ak):
    l = 0
    teta0 = A0[0] / ak[0]
    for i in range(1, len(A0)):
        teta = A0[i] / ak[i]
        if (teta < teta0):
            teta = i
            teta0 = teta
    return l

def update_delta(delta, al, k):
    print(delta)
    print(al)
    print(k)
    for j in range(len(delta) - 1):
        delta[j] = delta[j] - (al[j] / al[k]) * delta[k]
    return delta

def update_a(a, al, k):
    for i in range(len(a[0])):
        for j in range(len(a.T[0])):
            if (k == i):
                a[j, k] = al[j] / al[k]
                continue
            a[j, i] = a[j, i] - al[j] * (a[k, i] / al[k])
    return a

def iteration(a, c, basis):
    C = []
    for i in basis:
        C.append(c[i])
    print('C = ', C)
    C = np.array(C)
    delta = calculate_delta(a, c, C)
    print('delta = ', delta)
    k = find_k(delta)
    print('k = ', k)
    print('Оптимальность ', check_optimality(delta))
    step_3 = step3(a.T[k])
    print('step3 ', step_3)
    print('basis ', basis)
    step_4 = step4(a.T[0], a.T[k])
    print('step4 ', step_4)
    basis[step_4] = k
    print('basis ', basis)
    C[step_4] = c[k]
    print('C = ', C)
    a = update_a(a, a[step_4], k)
    print('updated a ', a)
    delta = update_delta(delta, a[step_4], k)
    print('update delta ', delta)
    return a, delta, basis

def Simplex(a, b, c):
    added_basis = find_basis(a)
    basis = []
    if (len(added_basis) < len(a)):
        a, c, basis = enter_additional_variables(a, c, added_basis)
    print('a = ', a)
    print('basis = ', basis)
    _basis = []
    for i in basis:
        _basis.append(i[1])
    print(_basis)
    print('c = ', c)
    a_new = np.zeros((len(a.T[0]), len(a[0]) + 1))
    a_new.T[0] += b
    for i in range(1, len(a_new[0])):
        for j in range(len(a_new.T[0])):
            a_new[j][i] += a[j][i - 1]
    print(a_new)
    isOptimal = False
    isValid = False
    count = 0
    while (isOptimal == False and isValid == False):
        print('count = ', count)
        a_new, delta, _basis = iteration(a_new, c, _basis)
        isOptimal = check_optimality(delta)
        isValid = check_validity(a_new.T[0])
        count += 1
    print(a_new)
    print(delta)
    print(basis)
    print(count)
    return

Simplex(np.array(a_l1), np.array(b_l1), np.array(c_new1))

f1.close()
f2.close()
f3.close()