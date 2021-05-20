import numpy as np
from scipy.optimize import minimize


def func(x): return (x[0] ** 2 + 1.5 * x[1] ** 2 - 2 * x[0] * x[1] + 4 * x[0] - 8 * x[1])


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

eps = 10 ** (-2)

teta = 0.2

x0 = np.array([1, 1])

def F(x):
    res = x[0] ** 2 + 3 * x[1] ** 2 - 3 * x[0] * x[1] - 6 * x[1]
    return res

def grad_F(x):
    res1 = 2 * x[0] - 3 * x[1] + 1
    res2 = 6 * x[1] - 3 * x[0] - 6
    return np.array([res1, res2])

# def gradient(_x0):
#     x = _x0
#     _F = F(x)
#     while (abs(_F) > eps):
#         new_x = x - teta * grad_F(x)
#         _F = F(new_x)
#         x = new_x
#     print(x)
#     return

def find_lambda(grad, x):
    lamb = (2 * grad[0] * x[0] + 6 * x[1] + grad[0] - 6 * grad[1] - 3 * grad[1] * x[0] - 3 * grad[0] * x[1]) / (6 * grad[0] * grad[1] - 2 * grad[0] ** 2 - 6 * grad[1])
    return lamb

def gradient(_x0):
    x = _x0
    s0 = -1 * grad_F(x)
    lamb = find_lambda(s0, x)
    x_new = x + lamb * s0
    print('lamb = ', lamb)
    return x_new

def start_gradient(_x0):
    x = _x0
    _F = F(x)
    count = 0
    while(abs(_F) > eps):
        x_new = gradient(x)
        _F_new = F(x_new)
        x = x_new
        count += 1
        print(_F)
        print(x)
        print(count)
        if (_F_new == _F):
            break
        _F = _F_new
    return

start_gradient(x0)
