import numpy as np
from scipy.optimize import minimize


def func(x): return (x[0] ** 2 + 3 * x[1] ** 2 - 3 * x[0] * x[1] - 6 * x[1])


def func_deriv(x):
    """ Derivative of objective function """
    dfdx0 = (2 * x[0] - 2 * x[1] + 4)
    dfdx1 = (-2 * x[0] + 3 * x[1] - 8)
    return np.array([dfdx0, dfdx1])


cons = ({'type': 'ineq', 'fun': lambda x: np.array([-x[0] - x[1] + 3]), 'jac': lambda x: np.array([-1.0, -1.0])},
        {'type': 'ineq', 'fun': lambda x: np.array([-x[0] + x[1] + 1]), 'jac': lambda x: np.array([-1.0, 1.0])},
        {'type': 'ineq', 'fun': lambda x: np.array([x[0]]), 'jac': lambda x: np.array([1.0, 0.0])},
        {'type': 'ineq', 'fun': lambda x: np.array([x[1]]), 'jac': lambda x: np.array([0.0, 1.0])})
res = minimize(func, [2.0, 4.0], jac=func_deriv, constraints=cons)
print(res)

print('---------------------------------------------------------------------------------------')

x0 = np.array([4, 3])

eps = 10 ** (-8)

def F(x):
    res = x[0] ** 2 + 3 * x[1] ** 2 - 3 * x[0] * x[1] + x[0] - 6 * x[1]
    return res

def grad_F(x):
    res1 = 2 * x[0] - 3 * x[1] + 1
    res2 = 6 * x[1] - 3 * x[0] - 6
    return np.array([res1, res2])

def a(x):
    return 2 * x[0] - 3 * x[1] + 1

def b(x):
    return 6 * x[1] - 3 * x[0] - 6

def find_lambda(x):
    lamb = (2 * a(x) * x[0] - 3 * a(x) * x[1] + a(x) - 3 * b(x) * x[0] + 6 * b(x) * x[1] - 6 * b(x)) / (2 * a(x) ** 2 - 6 * a(x) * b(x) + 6 * b(x) ** 2)
    return lamb

def start_gradient(_x0):
    x = _x0
    count = 0
    while (True):
        grad = grad_F(x)
        if (abs(grad[0]) < eps and abs(grad[1]) < eps):
            break
        s = (-1) * grad
        lamb = find_lambda(x)
        x_new = x + lamb * s
        x = x_new
        _F_new = F(x_new)
        count += 1
        print(x)
        print(_F_new)
        print(count)
    return

start_gradient(x0)

my_res = minimize(F, [1.0, 1.0], jac=grad_F)

print(my_res)