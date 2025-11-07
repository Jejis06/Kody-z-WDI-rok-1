def mnozenie_tablicowe(num1:list[int], num2:list[int]) -> list[int]:
    N = len(num1)
    M = len(num2)
    res = [0 for _ in range(N + M)]
    for i in range(N-1, -1, -1):
        for j in range(M-1, -1, -1):
            res[i + j + 1] +=  num1[i] * num2[j]

    for i in range(N+M-1, 0, -1):
        res[i - 1] += res[i] // 10
        res[i] %= 10


    return res
#
# def mno(a, b):
#     N = len(a)
#     M = len(b)
#     res = [0 for _ in range(N+M)]
#
#     for i in range(N):
#         for j in range(M):
#             res[i+j + 1] += a[i] * b[j]
#
#     for i in range(N+M - 1, 0, -1):
#         res[i-1] += res[i] // 10
#         res[i] %= 10
#     return res

# def dzie(a:list[int], b:int) -> list[int]:
#     N = len(a)
#     res = [0 for _ in range(N)]
#     r = 0
#     for i in range(N):
#         r = r * 10 + res[i]
#         res[i] = r//b
#         r %= b
#     return res

# def dod(a:list[int], b:list[int]) ->  list[int]:
#     assert len(a) == len(b)
#     N = len(a)
#     res = [0 for _ in range(N + 1)]
#     for i in range(N-1, -1, -1):
#         sum = a[i] + b[i] + res[i+1]
#         res[i+1] = sum % 10
#         res[i] += sum // 10
#     return res

def dzielenie_tablicowe(num1:list[int], num2:int) -> list[int]:
    N = len(num1)
    res = [0 for _ in range(N)]
    carry = 0

    for i in range(N):
        carry += carry * 10 + num1[i]
        res[i] = carry // num2
        carry = carry % num2
    return res

def dodawanie_tablicowe(num1:list[int], num2:list[int]) -> list[int]:
    assert len(num1) == len(num2)
    N = len(num1)
    res = [0 for _ in range(N+1)]

    for i in range(N-1, -1, -1):
        t = (num1[i] + num2[i] + res[i+1])
        res[i+1] = t % 10
        res[i] += t // 10

    return res


def fib(n: int) -> None:
    a = b = 1
    while a < n:
        print(a)
        a, b = b, a + b

def NWD(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a%b
    return a

def NWW(a:int, b:int) -> int:
    return (a*b)//NWD(a,b)

def Czy_palindrom(a: str) -> bool:
    N = len(a)
    i = N-1
    j = 0
    while i > j:
        if a[i] != a[j]:
            return False
        i -= 1
        j += 1
    return True

def square_fill(arr: list[list[int]]) -> None:
    N = len(arr)
    k = 1
    a = 0
    b = N-1
    while a < b:
        for i in range(a,b): arr[a][i] = k; k += 1
        for i in range(a,b): arr[i][b] = k; k += 1
        for i in range(b, a, -1): arr[b][i] = k; k += 1
        for i in range(b, a, -1): arr[i][a] = k; k += 1

        a += 1
        b -= 1
    if N%2>=1: arr[a][b] = k
    for i in range(N):
        for j in range(N):
            print(arr[i][j], end=' ')
        print()




a = [9,9,9,9,9,9,6,6,9,4,2,4,0,0,1]
b = [0,0,0,0,0,1,1,1,2,3,4,5,6,7,8]
print(''.join(str(i) for i in a), end=' * ')
print(''.join(str(i) for i in b))
print("=")
print(''.join(str(i) for i in mno(a, b)))

print()
print(''.join(str(i) for i in a), end=' * ')
print(''.join(str(i) for i in b))
print("=")
print(''.join(str(i) for i in mnozenie_tablicowe(a, b)))

exit(0)
N = 5
arr = [[0 for _ in range(N)] for _ in range(N)]
square_fill(arr)



fib(int(1e6))
print(NWD(8, 4))
print(NWW(8, 4))

a = ["aaa", "aaaa", "ababbaba", "kajak", "dupppppa"]
for x in a:
    print(Czy_palindrom(x))


a = [9,9,9,9,9,9,6,6,9,4,2,4,0,0,1]
b = [0,0,0,0,0,1,1,1,2,3,4,5,6,7,8]
print(''.join(str(i) for i in a), end=' + ')
print(''.join(str(i) for i in b))
print("=")
print(''.join(str(i) for i in dodawanie_tablicowe(a, b)))

print()
print(''.join(str(i) for i in a), end=' * ')
print(''.join(str(i) for i in b))
print("=")
print(''.join(str(i) for i in mnozenie_tablicowe(a, b)))
