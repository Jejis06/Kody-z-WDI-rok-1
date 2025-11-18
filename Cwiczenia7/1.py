'''
Zadanie 144. Korzystając z zależności: n
k

=
n−1
k−1

+
n−1
k

proszę napisać funkcję obliczającą wartość
symbolu Newtona dla argumentów n i k
'''
from functools import cache

@cache
def symb(n, k) -> int:
    if n == k or k == 0: return 1
    return symb(n-1 ,k-1) + symb(n-1, k)

print(symb(144, 21))
