'''
Zadanie 146. ”Waga” liczby jest określona jako liczba różnych czynników pierwszych liczby. Na przykład
waga(1)=0, waga(2)=1, waga(6)=2, waga(30)=3, waga(64)=1. Dana jest tablica T[N] zawierająca liczby
naturalne. Proszę napisać funkcję, która sprawdza czy można elementy tablicy podzielić na 3 podzbiory o
równych wagach. Do funkcji należy przekazać wyłącznie tablicę, funkcja powinna zwrócić wartość typu Bool.
'''


def waga(n: int) -> int:
    i = 2
    w = 0
    while n > 1:
        if n % i == 0:
            w += 1
            while n % i == 0:
                n //= i
        i += 1
    return w


def podzial(T, p=0, s1=0, s2=0, s3=0) -> bool:
    N = len(T)
    if p == N:
        return s1 == s2 == s3
    return podzial(T, p + 1, s1 + T[p], s2, s3) or podzial(T, p + 1, s1, s2 + T[p], s3) or podzial(T, p + 1, s1, s2, s3 + T[p])


def zad(T: list[int]) -> bool:
    N = len(T)
    Tw = [waga(i) for i in T]

    if sum(Tw) % 3 != 0:
        return False

    return podzial(Tw)


print(waga(64))
print(waga(30))
T = []
