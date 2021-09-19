import numpy as np
import math
import matplotlib.pyplot as plt
import pandas as pd


operators = ['{', '[', '(', '"', '.']
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
    # while(False in new_array[i]):
    #     new_array[i].remove(False)


operators_count = []
for oper in operators:
    count = 0
    for i in new_array:
        for j in i:
            if j == oper:
                count += 1
                #j = False #нужно подумать об этом
    operators_count.append([oper, count])
print(operators_count)

for i in new_array:
    print(i)

f.close()