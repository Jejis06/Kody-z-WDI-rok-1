from math import isqrt
# zadanie 66

#N = int(input("N: "))
N = int(1e6)

def getPrimes(N) -> int:
    if N < 2: return 0
    sito = [True for _ in range(N+1)]
    sito[0] = sito[1] = False

    for i in range(2, isqrt(N)+1):
        if sito[i]:
            for j in range(i*i, N+1, i):
                sito[j] = False

    return sum(sito)

print(getPrimes(N))
