from random import randint
from math import gcd

def isprime(n):
    if n < 2: return False
    if n == 2 or n == 3: return True
    if n % 2 == 0: return False
    if n % 3 == 0: return False
    i = 5
    while i*i <= n:
        if n%i == 0 or n%(i+2) == 0:
            return False
        i += 6
    return True

# fermat - male twierdzenie
def isprime2(n, x=100):
    if n < 2 : return False
    if n == 2 or n == 3: return True
    if n % 2 == 0: return False
    for i in range(x):
        a = randint(2, n-1)
        if gcd(a,n) != 1: return False
        if pow(a, n-1, n) != 1: return False
    return True



N = int(input(":"))
print(isprime(N), isprime2(N))