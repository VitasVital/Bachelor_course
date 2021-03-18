import numpy as np
from scipy.optimize import linprog

a_l = [[55, 69, 77, 58, 93],
       [87, 99, 60, 85, 76],
       [94, 56, 86, 55, 64]]
b_l = [2211, 4836, 3712]
c = [74, 99, 91, 87, 95]
c_new = np.dot(c, -1)

res_lin = linprog(c_new, a_l, b_l)
print(res_lin)
print(np.dot(res_lin.fun, -1))