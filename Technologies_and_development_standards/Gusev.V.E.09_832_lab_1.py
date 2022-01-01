import numpy as np
import copy

f = open('text_of_program.txt', 'r', encoding='utf-8')

array = [row.strip() for row in f]
for i in array:
    if(i == ''):
        array.remove(i) #удалить пробелы

new_array = []
for i in array:
    new_array.append(list(i)) #разбить строки на символы

for i in range(len(new_array) - 1): #удаление всех string в строках
    start_symbol = False
    for j in range(len(new_array[i]) - 1):
        if (start_symbol == False and new_array[i][j] == '"'):
            start_symbol = True
        elif (start_symbol == True and new_array[i][j] == '"'):
            start_symbol = False
            new_array[i][j] = False
        elif (start_symbol == True):
            new_array[i][j] = False

text_without_string = ""

for i in range(len(new_array)):
    for j in range(len(new_array[i])):
        text_without_string += str(new_array[i][j])
    text_without_string += '\n'

print(text_without_string)

operators = ['{', '[', '(', '"', '.', ';', '==', '|=', '^=', '>=', '<=', '>=', '+=', '-=',
             '*=', '/=', '%=', '&=', '++', '--', '&&', '||', '~', '<<', '>>',
             'sizeof', 'TypeOf', 'new', 'ReadLine', 'Parse', 'WriteLine', 'if', 'for', 'while', '?:', 'is'
             'switch', 'do', 'foreach', 'break', 'continue', 'goto', 'return', 'yield', 'throw', 'try'
             'await', 'fixed', 'lock']
operators_single = ['|', '^', '>', '<', '+', '-', '*', '/', '%', '=', '&', '!']
operators_count = []
operators_single_count = []

for i in operators:
    operators_count.append([i, text_without_string.count(i)])

new_array_single = copy.deepcopy(new_array)
for i in operators_single:
    count = 0
    for j in range(len(new_array_single)):
        for q in range(len(new_array_single[j]) - 1):
            if i == new_array_single[j][q] and i != new_array_single[j][q + 1]:
                count += 1
                new_array_single[j][q] = False
                new_array_single[j][q + 1] = False
    operators_single_count.append([i, count])

operators_count += operators_single_count
print('Операторы ', operators_count)

operands = []

for j in range(len(new_array)):
    for q in range(len(new_array[j]) - 1):
        if new_array[j][q] == '=' and (new_array[j][q - 1] in operators_single) == False:
            position = q - 1
            operand = ''
            while new_array[j][position] == ' ':
                position -= 1
            while new_array[j][position] != ' ':
                operand += new_array[j][position]
                position -= 1
                if (position == -1):
                    break
            operand = operand[::-1]
            if (operand in operands) == False:
                operands.append(operand)

operands_count = []
for i in operands:
    operands_count.append([i, text_without_string.count(i)])
print('Операнды ', operands_count)

operators_res = []
for i in operators_count:
    if i[1] != 0:
        operators_res.append(i)

N = len(operators_res) * np.log(len(operators_res)) + len(operands_count) * np.log(len(operands_count)) #Теоритическая длина программы
print('Теоретическая длина программы ', N)
N1 = 0 #общее число операторов
for i in operators_res:
    N1 += i[1]
N2 = 0 #общее число операндов
for i in operands_count:
    N2 += i[1]

V = (N1 + N2) * np.log(len(operators_res) + len(operands_count)) #Объём программы
print('Объём программы ', V)

f.close()