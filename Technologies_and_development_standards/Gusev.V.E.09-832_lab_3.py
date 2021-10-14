import numpy as np
from random import randint

N = 10

A = np.array([randint(-10, 10) for i in range(N)], dtype=np.float64)

print('Сгенерированный массив А\n', A)

A = A ** 2

print('Массив квадратов чисел массива А\n', A)

sum_A = [A[0]]

for k in range(1, N):
    sum_A.append(sum_A[k - 1] * A[k])

print('Произведения элементов массива\n', sum_A)

print('K = ', np.argmax(sum_A), ' , произведение = ', sum_A[np.argmax(sum_A)])