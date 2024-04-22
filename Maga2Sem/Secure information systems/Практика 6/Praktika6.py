def gcd(A, B):
    while B != 0:
        A = A % B
        A, B = B, A
    return A


def Euler(number):
    result = 0
    for i in range(1, number):
        if (gcd(number, i) == 1):
            result += 1
    return result

def IsPrime(number):
    for i in range(2, number):
        if (number % i == 0):
            return False
    return True

for i in range(1, 1001):
    if (IsPrime(i)):
        print('IsPrime ', i)
    
for i in range(1, 1001):
    if (i % 2 == 0):
        print('odd ', i)

for i in range(1001, 2001):
    if (i % 2 != 0):
        print('even ', i)

for i in range(2001, 3001):
    if (IsPrime(i)):
        print('IsPrime ', i)