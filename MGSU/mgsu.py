import json

f = open('data.json', 'r', encoding='utf-8') # считываем json
dataset = json.load(f)['events_data'] # получаем объекты в events_data

client_count = 0 # инициализируем количество клиентов
for event in dataset: # циклом проверяем в каждом объекте events_data поле category
    if event['category'] in ['page', 'report']:
        client_count += 1

print(f'Количество клиентов совершившие действия с категориями page или report = {client_count}')