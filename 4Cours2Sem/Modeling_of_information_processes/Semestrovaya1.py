import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import linprog
import pandas as pd
import random as rn

n = 10
b = 30
k = 6
alpha = 0
betta = [] # [2, 10]
for i in range(10):
    betta.append(rn.randrange(2, 11))

df = pd.DataFrame(betta)
df.to_excel('./res_betta.xlsx')

my_c = []
x = [i for i in range(1, n + 1)]

for i in range(1, n + 1):
    c_i = 3 + 2 * np.sin(k * i)
    print(f'c({i}) = {c_i}')
    my_c.append(c_i)

fig = plt.figure()
plt.bar(x, my_c, align='center') # A bar chart
plt.xlabel('i')
plt.ylabel('c(i)')
plt.show()

lhs_ineq = np.vstack([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                      [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
                      np.diag(np.full(n, 1))])

rhs_ineq = [b, -b]
rhs_ineq.extend(betta)
print(rhs_ineq)

opt = linprog(c=my_c, A_ub=lhs_ineq, b_ub=rhs_ineq, method="revised simplex")
print(opt)

res = opt.x * my_c
print('x(i) * c(i) = ' + str(res))

fig = plt.figure()
plt.bar(x, res, align='center')
plt.xlabel('i')
plt.ylabel('x(i) * c(i)')
plt.show()

df = pd.DataFrame(my_c)
df.to_excel('./res_c.xlsx')

df = pd.DataFrame(opt.x)
df.to_excel('./res_opt_x.xlsx')

df = pd.DataFrame(res)
df.to_excel('./res_res.xlsx')