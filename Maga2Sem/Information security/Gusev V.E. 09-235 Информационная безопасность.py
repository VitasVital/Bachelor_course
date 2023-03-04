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

def step4(B):

    return

def task1():
    input_text = input('Введите текст')
    bit_text = step1(input_text)
    print('Битовая последовательность:\n', bit_text)
    r = 25
    binary_text = step2(bit_text, r)
    print('Бинарная последовательность:\n', binary_text)
    B = step3(binary_text, r)
    step4(B)

task1()