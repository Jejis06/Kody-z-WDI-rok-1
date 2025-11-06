from math import sqrt
mem = {}
def a(n):
    if n == 1: return 3
    if n in mem: return mem[n]
    mem[n] = (4 * a(n - 1) + 10)/(4 + a(n-1))
    return mem[n]


for i in range(1, 100):
    if a(i) - sqrt(10) == 0:
        print(a(i), i)
        break

