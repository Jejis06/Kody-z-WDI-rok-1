'''
Zadanie 89. Dwie liczby naturalne są 4-zgodne, jeżeli po zapisaniu ich w systemie o podstawie 4, zbiory
cyfr występujące w liczbie są identyczne. Na przykład:
13 = 31(4) i 23 = 113(4)
18 = 102(4) i 33 = 201(4)
107 = 1223(4) i 57 = 321(4).
Dana jest tablica T[N] zawierająca N liczb naturalnych. Proszę napisać funkcję, która zwraca długość najdłuższego podciągu (niekoniecznie spójnego) złożonego z liczb 4-zgodnych.
'''
n = 23
res = 0
while n > 0:
    res |= 1 << (n%4)
    n //= 4

print(bin(res))

