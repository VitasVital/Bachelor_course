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

#Оптимальность. Все дельта должны быть неположительными
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
    return [l, ind]

def update_delta(delta, al, k):
    new_delta = []
    for j in range(len(delta)):
        new_delta.append(delta[j] - (al[j] / al[k]) * delta[k])
    return new_delta

def update_a(a, al, k, l):
    a_new = np.zeros((len(a.T[0]), len(a[0])))
    for j in range(len(a[0])):
        for i in range(len(a.T[0])):
            if (l == i):
                a_new[i, j] = al[j] / al[k]
                continue
            a_new[i, j] = a[i, j] - al[j] * (a[i, k] / al[k])
    return a_new
#доделать
def help_table(a, delta):
    ind = 0
    for i in range(len(a.T[0])):
        if a.T[0, i] < 0:
            ind = i
            break
    res = []
    min = 0
    minind = 0
    min_finded = False #минимальный по модулю
    for i in range(1, len(a[0])):
        if (a[ind, i] != 0):
            res.append(delta[i] / a[ind, i])
            if (min_finded == False):
                min = delta[i] / a[ind, i]
                minind = i
                min_finded = True
                continue
            if (abs(min) > abs(delta[i] / a[ind, i]) and delta[i] / a[ind, i] != 0):
                min = delta[i] / a[ind, i]
                minind = i
        else:
            res.append(0)
    return [res, minind, ind]

def iteration(a, c, basis, delta, C):
    print('\nstart-----------------------------------')
    k = find_k(delta)
    print('k = ', k)
    step_3 = step3(a.T[k], basis)
    print('step3 ', step_3)
    step_4 = step4(a.T[0], a.T[k], basis, step_3)
    print('step4 ', step_4)
    basis[step_4[1]] = k
    print('new basis ', basis)
    C[step_4[1]] = c[k - 1]
    print('C = ', C)
    new_a = update_a(a, a[step_4[1]], k, step_4[1])
    print('updated a ', a)
    delta = update_delta(delta, new_a[step_4[1]], k)
    print('update delta ', delta)
    print('stop-----------------------------------')
    return new_a, delta, basis, C

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
    count = 0
    C = []
    for i in _basis:
        C.append(c[i])
    delta = calculate_delta(a_new, c, C)
    isOptimal = check_optimality(delta)
    isValid = check_validity(a_new.T[0])
    while (isOptimal == False or isValid == False):
        count += 1
        print('count = ', count)
        if (isValid == False):
            dvoistvenniy = help_table(a_new, delta)
            print('двойственный ', dvoistvenniy)
            new_a = update_a(a_new, a_new[dvoistvenniy[2]], dvoistvenniy[1], dvoistvenniy[2])
            print('updated a двйосвенный ', new_a)
            delta = update_delta(delta, new_a[dvoistvenniy[2]], dvoistvenniy[1])
            print('update delta двойсвенный ', delta)
            count += 1
        a_new, delta, _basis, C = iteration(a_new, c, _basis, delta, C)
        isOptimal = check_optimality(delta)
        isValid = check_validity(a_new.T[0])
        print('Optimal ', isOptimal, ' valid ', isValid)
    print('result a =', a_new)
    print('result a0 =', a_new.T[0])
    print('result delta =', delta)
    print('result basis =', _basis)
    print('result count =', count)
    print('F = ', delta[0])
    return

Simplex(np.array(a_l1), np.array(b_l1), np.array(c_new1))

f1.close()
f2.close()
f3.close()