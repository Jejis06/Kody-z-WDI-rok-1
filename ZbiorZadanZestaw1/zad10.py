import sys
N = int(input(":"))

a = 1
b = 1
while a*b < N:
    a, b = b, a + b
if a * b == N:
    print("TAK")
else: print("NIE")