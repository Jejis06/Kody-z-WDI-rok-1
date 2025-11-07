def NWD(a, b):
    while b != 0:
        a,b = b,a%b
    return a

def max_multiplication(n, base) -> int:
    a = 0
    wykl = 1
    max_val = 0
    while n > 0:
        a += n%base * wykl
        b = n // base

        if NWD(a, b) == wykl:
            max_val = max(max_val, a*b)

        wykl *= base
        n //= base
    return max_val


n = int(input())

maxbase = 2
max_reach = 0

for i in range(2, 17):
    t = max_multiplication(n, i)
    if t > max_reach:
        max_reach = t
        maxbase = i

print(maxbase)