from math import ceil, floor
def sumDziel(n):
    if n <= 1: return 0
    i = 2
    sum = 1
    while i * i <= n:
        if n % i == 0:
            sum += i
            if i != n // i: # dodajemy sparowany dzielnik
                sum += n // i
        i += 1
    return sum


for i in range(1, int(1e6)):
    j = sumDziel(i)
    if j > i and j < int(1e6):
        if sumDziel(j) == i:
            print(i, j)