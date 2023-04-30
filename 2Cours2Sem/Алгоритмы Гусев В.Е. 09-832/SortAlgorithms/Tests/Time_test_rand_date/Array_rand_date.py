import random
from datetime import date, timedelta

d1 = date(2018, 8, 13)  # начальная дата
d2 = date(2018, 11, 20)  # конечная дата
rand_date_100=[]
delta = d2 - d1         # timedelta
if delta.days<=0:
    print ("Ругаемся и выходим")
for i in range(delta.days + 1):
    rand_date_100.append(d1 + timedelta(i))
random.shuffle(rand_date_100)

d1 = date(1988, 8, 13)  # начальная дата
d2 = date(2015, 12, 29)  # конечная дата
rand_date_10000=[]
delta = d2 - d1         # timedelta
if delta.days<=0:
    print ("Ругаемся и выходим")
for i in range(delta.days + 1):
    rand_date_10000.append(d1 + timedelta(i))
random.shuffle(rand_date_10000)

d1 = date(1, 1, 1)  # начальная дата
d2 = date(2738, 11, 28)  # конечная дата
rand_date_1000000=[]
delta = d2 - d1         # timedelta
if delta.days<=0:
    print ("Ругаемся и выходим")
for i in range(delta.days + 1):
    rand_date_1000000.append(d1 + timedelta(i))
random.shuffle(rand_date_1000000)
