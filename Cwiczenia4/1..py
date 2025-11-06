_ = '''
Zadanie 85. Napisać program, który wyznacza n-tą cyfrę po przecinku rozwinięcia dziesiętnego wartości
sqrt(2). Program powinien działać poprawnie dla n < 100


an+1 = 2/an + an
'''
# True == 2
def power2(arr) -> bool:
    n = len(arr)

    res = [0 for _ in range(2*n)]
    for i in range(n):
        for j in range(n):
            res[i+j] += arr[i] * arr[j]

    for i in range(2*n-1, 0, -1):
        res[i-1] += res[i]//10
        res[i] %= 10


    return res[0] == 2



def zad(n) -> int:
    pierw = [0 for _ in range(n+1)]
    pierw[0] = 1
    for i in range(1, n+1):
        for k in range(1, 10):
            pierw[i] = k
            if power2(pierw):
                pierw[i] -= 1
                break
    return pierw[n]


n = int(input(":"))
print(zad(n))