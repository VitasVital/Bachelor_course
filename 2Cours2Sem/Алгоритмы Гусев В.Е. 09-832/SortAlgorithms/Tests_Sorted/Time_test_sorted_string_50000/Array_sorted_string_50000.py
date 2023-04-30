import random
import string

def build_rand_string(size, lenght):
    l=[]
    for i in range(lenght):
        l.append(''.join(random.choice(string.ascii_letters) for _ in range(size)))
    return l

sorted_string_50000_100=build_rand_string(50000,100)
l=sorted_string_50000_100[25:75]
l.sort()
sorted_string_50000_100[25:75]=l

sorted_string_50000_10000=build_rand_string(50000,10000)
l=sorted_string_50000_10000[2500:7500]
l.sort()
sorted_string_50000_10000[2500:7500]=l

# sorted_string_50000_1000000=build_rand_string(50000,1000000)
# l=sorted_string_50000_1000000[250000:750000]
# l.sort()
# sorted_string_50000_1000000[250000:750000]=l