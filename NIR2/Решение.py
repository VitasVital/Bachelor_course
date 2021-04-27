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
    delta.append(a.T[0] @ C)
    for _c in range(len(c)):
        res = a.T[_c + 1] @ C - c[_c]
        delta.append(res)
    return np.array(delta)

def find_k(delta):
    res = 1
    for i in range(1, len(delta)):
        if (delta[i] > delta[res]):
            res = i
    return res

def step3(ak, basis):
    res = []
    for i in range(len(ak)):
        if (ak[i] > 0):
            res.append(basis[i])
    return res

def step4(A0, ak, basis, step_3):
    l = 0
    ind = 0
    teta0 = 0
    first_teta = False
    for i in range(0, len(A0)):
        if (basis[i] in step_3 == False):
            continue
        if (first_teta == False):
            teta0 = A0[i] / ak[i]
            l = basis[i]
            first_teta = True
            continue
        if (teta0 > A0[i] / ak[i]):
            teta0 = A0[i] / ak[i]
            l = basis[i]
            ind = i
    return l, ind

def update_delta(delta, al, k):
    print(delta)
    print(al)
    print(k)
    for j in range(len(delta)):
        new_delta = delta[j] - (al[j] / al[k]) * delta[k]
        delta[j] = new_delta
    return delta

def update_a(a, al, k):
    print('up a ', a)
    print('up al ', al)
    for i in range(len(a[0])):
        for j in range(len(a.T[0])):
            if (k == i):
                a_new = al[j] / al[k]
                a[j, i] = a_new
                continue
            a_new = a[j, i] - al[i] * (a[k, i] / al[k])
            a[j, i] = a_new
    return a

def iteration(a, c, basis):
    print('start-----------------------------------')
    C = []
    for i in basis:
        C.append(c[i])
    print('C = ', C)
    C = np.array(C)
    delta = calculate_delta(a, c, C)
    print('delta = ', delta)
    k = find_k(delta)
    print('k = ', k)
    step_3 = step3(a.T[k], basis)
    print('step3 ', step_3)
    step_4 = step4(a.T[0], a.T[k], basis, step_3)
    print('step4 ', step_4)
    basis[step_4[1]] = step_4[0]
    print('basis ', basis)
    C[step_4[1]] = c[k]
    print('C = ', C)
    new_a = update_a(a, a[step_4[1]], k)
    print('updated a ', a)
    delta = update_delta(delta, a[step_4[1]], k)
    print('update delta ', delta)
    print('stop-----------------------------------')
    return new_a, delta, basis

def Simplex(a, b, c):
    added_basis = find_basis(a)
    basis = []
    if (len(added_basis) < len(a)):
        a, c, basis = enter_additional_variables(a, c, added_basis)
    print('a = ', a)
    print('basis = ', basis)
    _basis = np.array(basis).T[1]
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
    while (isOptimal == False or isValid == False):
        print('count = ', count)
        a_new, delta, _basis = iteration(a_new, c, _basis)
        isOptimal = check_optimality(delta)
        isValid = check_validity(a_new.T[0])
        print(isOptimal, ' ', isValid)
        count += 1
    print('result a =', a_new)
    print('result delta =', delta)
    print('result basis =', _basis)
    print('result count =', count)
    return

Simplex(np.array(a_l1), np.array(b_l1), np.array(c_new1))

f1.close()
f2.close()
f3.close()