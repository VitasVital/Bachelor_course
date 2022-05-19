f1 = open('id_identity.txt', 'r')
f2 = open('id_warehouse.txt', 'r')
id_identity = f1.read().splitlines()
id_warehouse = f2.read().splitlines()
print('Есть в идентити, но нет в отчёте')
for id in id_identity:
    if id not in id_warehouse:
        print(id)

print('Есть в отчёте, но нет в идентити')
for id in id_warehouse:
    if id not in id_identity:
        print(id)