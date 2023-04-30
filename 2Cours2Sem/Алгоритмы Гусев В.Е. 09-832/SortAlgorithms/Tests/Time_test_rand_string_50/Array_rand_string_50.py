import random
import string

def build_rand_string(size, lenght):
    l=[]
    for i in range(lenght):
        l.append(''.join(random.choice(string.ascii_letters) for _ in range(size)))
    return l

rand_string_50_100=build_rand_string(50,100)
rand_string_50_10000=build_rand_string(50,10000)
rand_string_50_1000000=build_rand_string(50,1000000)