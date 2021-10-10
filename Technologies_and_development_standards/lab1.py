import numpy as np
import math
import matplotlib.pyplot as plt
import pandas as pd
import re
import string
import copy

f = open('program.txt', 'r')

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
            #new_array[i][j] = False
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

operators = ['{', '[', '(', '"', '.', ';', '==', '|=', '^=', '>=', '<=', '>=', '+=', '-=', '*=', '/=', '%=', '&=', '++', '--', '&&', '||', '!', '~', '<<', '>>',
             'sizeof', 'TypeOf', 'new', 'ReadLine', 'Parse', 'WriteLine', 'if', 'for', 'while', '?:', 'is'
             'switch', 'do', 'foreach', 'break', 'continue', 'goto', 'return', 'yield', 'throw', 'try'
             'await', 'fixed', 'lock']
operators_single = ['|', '^', '>', '<', '+', '-', '*', '/', '%', '=', '&']
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
print(operators_count)

initializing_variables = ['=', 'new']
operands = []
for i in initializing_variables:
    for j in range(len(new_array)):
        for q in range(len(new_array[j]) - 1):
            if i == new_array[j][q]:
                print(i)
                position = q - 1
                operand = ''
                while new_array[j][position] == ' ':
                    position -= 1
                while new_array[j][position] != ' ':
                    operand += new_array[j][position]
                #if operand in operands == False:
                operands.append(operand)

print(operands)

f.close()