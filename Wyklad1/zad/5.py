from random import randint
from math import gcd

def nwd(a,b):
    while b != 0:
        a, b = b, a % b
    return a

def checkPrime(p, n=100):
    if p < 2: return False
    if p == 2 or p == 3: return True
    if p % 2 == 0: return False

    for i in range(n):
        a = randint(2, p-1)
        if gcd(a,p) != 1: return False
        if pow(a, p-1, p) != 1: return False
    return True


start = pow(10, 99)
print(start, len(str(start)))
end = pow(10, 100) -1
print(end, len(str(end)))
while start <= end:
    if checkPrime(start):
        print(f"Found {start} of length {len(str(start))}")
        break
    start += 1

