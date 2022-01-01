import numpy as np
from scipy.optimize import minimize
import random as rn
import itertools as it

N = 3

k = []

stuff = [i for i in range(1, N + 1)]
for L in range(0, len(stuff)+1):
    for subset in it.combinations(stuff, L):
        k.append(list(subset))

res_array = []

for item in it.permutations(range(N), N):
    res_array.append([i + 1 for i in list(item)])

print(res_array)

V_k = [rn.randrange(100, 600) for i in res_array]

print(V_k)

