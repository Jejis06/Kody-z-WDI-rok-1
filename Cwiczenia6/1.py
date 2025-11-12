"""
Zadanie 143. Dany jest ciąg N liczb naturalnych, z którego wybieramy spójny fragment o długości K
(1 < K < N). Pomiędzy wszystkie elementy wybranego fragmentu możemy wstawiać operatory dodawania
albo mnożenia, tak aby powstało wyrażenie arytmetyczne. W powstałym wyrażeniu nie mogą wystąpić dwa
jednakowe operatory obok siebie. Interesuje nas znalezienie takiego fragmentu ciągu, który pozwala zbudować wyrażenie o wartości będącej liczbą pierwszą. Proszę napisać funkcję f ind max(T), która dla ciągu
zawartego w tablicy T, wyznaczy wartość największej liczby pierwszej, jaką można znaleźć. Jeżeli taki podciąg nie istnieje, funkcja powinna zwrócić wartość zero.
Na przykład dla ciągu: 7,8,6,4,7,3 funkcja powinna zwrócić wartość 83
Możliwe podciągi dające liczby pierwsze to:
7 + 8 ∗ 6 + 4 = 59
7 + 8 ∗ 6 + 4 ∗ 7 = 83
6 ∗ 4 + 7 = 31
4 + 7 = 11
"""

def isprime(n) -> int:
    i = 2
    while i * i <= n:
        if n % i == 0:
            return 0
        i += 1
    return n

def find_max_t(T: list[int]) -> int:
    max_n = 0
    N = len(T)
    for p in range(N-1):
        for k in range(p+2, N+1):
            if k - p == N: continue

            sum1 = 0
            for i in range(p, k-1, 2): sum1 += T[i] * T[i+1]
            if (k-p) % 2 == 1: sum1 += T[k-1]

            sum2 = T[p]
            for i in range(p+1, k-1, 2): sum2 += T[i] * T[i+1]
            if (k-p) % 2 == 0: sum2 += T[k-1]

            max_n = max(max_n, isprime(sum1), isprime(sum2))
    return max_n

T = [7,8,6,4,7,3]
print(find_max_t(T))

