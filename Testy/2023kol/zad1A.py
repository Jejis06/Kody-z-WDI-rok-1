
def match_factors(a: int , b: int) -> bool:
    if b > a:
        a, b = b, a
    
    i = 2
    while i * i <= b:
        if i % b == 0:
            if i % a != 0: return False
            a //= i
            b //= i
        i += 1

    if b > 0:
        return a%b == 0
    return True 


def zgodne(T: list[int]) -> int:
    N = len(T)
    seen = [0 for _ in range(999 + 1)]
    num = 0
    for i in range(N-1):
        for j in range(min((N-1-i), 3)):
            if match_factors(T[i], T[j+i+1]):
                if not seen[T[i]]:
                    num += 1
                if not seen[T[i+j+1]]:
                    num += 1
                seen[T[i]] = seen[T[i+j+1]] = True

    return num




T = [2, 3, 4, 5, 7, 6, 23, 24, 12, 13, 14, 15, 16, 45]
print(zgodne(T))


