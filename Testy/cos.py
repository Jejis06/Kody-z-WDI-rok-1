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
