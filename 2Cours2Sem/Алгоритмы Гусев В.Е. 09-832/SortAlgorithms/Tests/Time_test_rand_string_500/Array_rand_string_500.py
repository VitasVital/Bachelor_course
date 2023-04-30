import random
import string

def build_rand_string(size, lenght):
    l=[]
    for i in range(lenght):
        l.append(''.join(random.choice(string.ascii_letters) for _ in range(size)))
    return l

rand_string_500_100=build_rand_string(500,100)
rand_string_500_10000=build_rand_string(500,10000)
rand_string_500_1000000=build_rand_string(500,1000000)