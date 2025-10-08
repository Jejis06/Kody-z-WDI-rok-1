from math import sqrt

N = int(input("N: "))

for a in range(1, N):
    for b in range(a, N):
        c2 = a * a + b * b
        c = int(sqrt(c2))
        if c * c == c2 and c < N:
            print(f"a: {a}, b: {b}, c: {c} ")