import random
import string

def build_rand_string(size, lenght):
    l=[]
    for i in range(lenght):
        l.append(''.join(random.choice(string.ascii_letters) for _ in range(size)))
    return l

rand_string_500000_100=build_rand_string(500000,100)
rand_string_500000_1000=build_rand_string(500000,1000)
rand_string_500000_10000=build_rand_string(500000,10000)