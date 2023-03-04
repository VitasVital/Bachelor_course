import numpy as np

def step1(input_text):
    bit_text = ''
    for char in input_text:
        bit_text += format(ord(char), '08b')
    return bit_text

def step2(bit_text, r):
    binary_text = bit_text
    while(len(binary_text) % r > 0):
        binary_text += '1'
    return binary_text

def step3(binary_text, r):
    B = []
    zeros_ones = '01010101010101010101'
    for ind in range(len(binary_text) // r):
        B_res = binary_text[ind * r:(ind + 1) * r] + zeros_ones
        B.append(B_res)
    return B

def step4(B1):
    n = 3
    m = 3
    k = 5
    A = np.arange(45).reshape(3, 3, 5) # Задаем матрицу A размером 3 x 3 х 5.
    ii = 0
    for i in range(0, n):  # Заполняет ее элементами вектора B1
        for j in range(0, m):
            for h in range(0, k):
                A[i][j][h] = B1[ii]
                ii += 1
    return A

def step5(A):
    V = []
    for k in range(0, 5):
        V_ind = ''
        for n in range(0, 3):
            for m in range(0, 3):
                V_ind += str(A[n][m][k])
        V.append(V_ind)
    return V

def task1():
    input_text = input('Введите текст')
    bit_text = step1(input_text)
    print('Битовая последовательность:\n', bit_text, '\n')
    r = 25
    binary_text = step2(bit_text, r)
    print('Бинарная последовательность:\n', binary_text, '\n')
    B = step3(binary_text, r)
    for B1 in B:
        A = step4(B1)
        V = step5(A)
        print('Блок B\n', B1)
        print('     Бинарные вектора V\n', '    ', V, '\n')

task1()