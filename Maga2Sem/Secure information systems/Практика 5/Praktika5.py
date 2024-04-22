import time
import sys
import random
from datetime import date
import pandas as pd

iteration = 0
def gcd(A, B):

    iteration = 0
    while B != 0:
        A = A % B
        A, B = B, A
        iteration += 1

    print("iteration ", iteration)
    return A


# начальное время
start_time = time.time()

sys.set_int_max_str_digits(15000)
input_A = random.randint(0, int("235" * 5000))
input_B = random.randint(0, int("467" * 5000))

gcd_res = gcd(input_A, input_B)
print("gcd ", gcd_res)
# конечное время
end_time = time.time()
 
# разница между конечным и начальным временем
elapsed_time = end_time - start_time
print('Elapsed time: ', elapsed_time)

file = open("otus.txt", "w")
file.write(f"input_A = {input_A}\n")
file.write(f"input_B = {input_B}\n")
file.write(f"gcd = {gcd_res}\n")
file.write(f"iteration = {iteration}\n")
file.write(f"date = {date.today()}\n")
file.close()

file1 = open("otus.csv", "w")
file1.write(f"input_A = {input_A}\n")
file1.write(f"input_B = {input_B}\n")
file1.write(f"gcd = {gcd_res}\n")
file1.write(f"iteration = {iteration}\n")
file1.write(f"date = {date.today()}\n")
file1.close()