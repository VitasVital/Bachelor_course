import numpy as np
import matplotlib.pyplot as plt

n = m = 10
N = 17
gi = []
hi = []
gi_help = []
hi_help = []

for ind in range(1, 11):
    gi_res = 1.5 + (1 / N) * np.sin(ind)
    hi_res = 1.5 + (1 / N) * np.cos(ind)
    gi.append(gi_res)
    hi.append(hi_res)
    gi_help.append([ind, gi_res])
    hi_help.append([ind, hi_res])

print('gi ', gi_help)
print('hi ', hi_help)

gi.sort()
hi.sort(reverse=True)
print('gi ', gi)
print('hi ', hi)

y = [y * 2 for y in range(10)]
plt.step(gi, y)
plt.step(hi, y)
plt.grid()
plt.show()
