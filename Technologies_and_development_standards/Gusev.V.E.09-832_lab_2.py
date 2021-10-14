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

lines_text_without_string = text_without_string.split('\n')

nodes_count = 0
for i in lines_text_without_string:
    if (len(i) > 1 and i.count('{') == 0 and i.count('}') == 0 and i.count('};') == 0):
        nodes_count += 1

print('Количество узлов = ', nodes_count)

edge_count = 0
for i in lines_text_without_string:
    if (len(i) > 1 and i.count('{') == 0 and i.count('}') == 0 and i.count('};') == 0):
        edge_count += 1
    if (i.count('if') > 0):
        edge_count += 2
    if (i.count('else') > 0):
        edge_count += 1
    if (i.count('for') > 0):
        edge_count += 1
    if (i.count('while') > 0):
        edge_count += 1
    if (i.count('switch') > 0):
        edge_count += 1
    if (i.count('case') > 0):
        edge_count += 1

print('Количество рёбер = ', edge_count)

V = edge_count - nodes_count + 2
print('Метрика Мак-Кейба = ', V)

f.close()