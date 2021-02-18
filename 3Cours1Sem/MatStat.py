import xlrd, xlwt

rb = xlrd.open_workbook('Задания Гусев В.Е. 09-832.xlsx')

sheet = rb.sheet_by_name('Данные')

val = sheet.row_values(2)[5]

list = []
for i in range(2,101):
    x = sheet.row_values(i)[5]
    y = sheet.row_values(i)[6]
    help_list = [x, y]
    list.append(help_list)

countB2 = 0
for i in list:
    if i[0] >= 114.05 and i[0] <= 116.05 and i[1] >= 83.05 and i[1] <= 85.05:
        countB2 += 1
print(countB2)

countC2 = 0
for i in list:
    if i[0] >= 116.05 and i[0] <= 118.05 and i[1] >= 83.05 and i[1] <= 85.05:
        countC2 += 1
print(countC2)

countD2 = 0
for i in list:
    if i[0] >= 118.05 and i[0] <= 120.05 and i[1] >= 83.05 and i[1] <= 85.05:
        countD2 += 1
print(countD2)

countE2 = 0
for i in list:
    if i[0] >= 120.05 and i[0] <= 122.05 and i[1] >= 83.05 and i[1] <= 85.05:
        countE2 += 1
print(countE2, '\n')


countB3 = 0
for i in list:
    if i[0] >= 114.05 and i[0] <= 116.05 and i[1] >= 81.05 and i[1] <= 83.05:
        countB3 += 1
print(countB3)

countC3 = 0
for i in list:
    if i[0] >= 116.05 and i[0] <= 118.05 and i[1] >= 81.05 and i[1] <= 83.05:
        countC3 += 1
print(countC3)

countD3 = 0
for i in list:
    if i[0] >= 118.05 and i[0] <= 120.05 and i[1] >= 81.05 and i[1] <= 83.05:
        countD3 += 1
print(countD3)

countE3 = 0
for i in list:
    if i[0] >= 120.05 and i[0] <= 122.05 and i[1] >= 81.05 and i[1] <= 83.05:
        countE3 += 1
print(countE3, '\n')


countB4 = 0
for i in list:
    if i[0] >= 114.05 and i[0] <= 116.05 and i[1] >= 79.05 and i[1] <= 81.05:
        countB4 += 1
print(countB4)

countC4 = 0
for i in list:
    if i[0] >= 116.05 and i[0] <= 118.05 and i[1] >= 79.05 and i[1] <= 81.05:
        countC4 += 1
print(countC4)

countD4 = 0
for i in list:
    if i[0] >= 118.05 and i[0] <= 120.05 and i[1] >= 79.05 and i[1] <= 81.05:
        countD4 += 1
print(countD4)

countE4 = 0
for i in list:
    if i[0] >= 120.05 and i[0] <= 122.05 and i[1] >= 79.05 and i[1] <= 81.05:
        countE4 += 1
print(countE4)


print(list)