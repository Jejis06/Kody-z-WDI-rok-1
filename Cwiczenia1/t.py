# liczby fibbonaciego na jedna zmienna do N

N = int(1e6)
E = 10 * N

# kodowanie x = E * a + b
x = E*1 + 1
while (x // E) < N:
    print(x // E)
    x = (x % E) * E + (x // E + x % E)
