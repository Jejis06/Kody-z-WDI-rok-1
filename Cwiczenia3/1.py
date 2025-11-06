# zad 64
from math import log2, ceil

# podst 2-16

def change_base(n, base) -> None:
    N = ceil(log2(n))
    num = [0 for _ in range(N)]
    ind = 0

    while n > 0:
        digit = n % base
        n //= base
        num[ind] = digit
        ind += 1

    for i in range(ind-1, -1, -1):
        digit = num[i]
        if digit > 9:
            digit = chr(65 + digit - 10)
        print(digit, end='')
    print()

n = int(input("n: "))
base = int(input("base: "))

change_base(n, base)