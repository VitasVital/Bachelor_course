from random import randint

sorted_integer_500000_100 = [randint(-250000, 250000) for i in range(100)]
l=sorted_integer_500000_100[25:75]
l.sort()
sorted_integer_500000_100[25:75]=l

sorted_integer_500000_10000 = [randint(-250000, 250000) for i in range(10000)]
l=sorted_integer_500000_10000[2500:7500]
l.sort()
sorted_integer_500000_10000[2500:7500]=l

sorted_integer_500000_1000000 = [randint(-250000, 250000) for i in range(1000000)]
l=sorted_integer_500000_1000000[250000:750000]
l.sort()
sorted_integer_500000_1000000[250000:750000]=l