from sys import setrecursionlimit
def isprime(x: int) -> bool:
    i = 2
    while i * i <= x:
        if x % i == 0:
            return False
        i += 1
    if x % i == 0:
        return False
    return True

def gen(A:int, B:int, c:int) -> int:
    if A == 0 and B == 0: return not isprime(c)
    r = 0
    if A > 0: r += gen(A-1, B, 2*c+1)
    if B > 0: r += gen(A, B-1, 2*c)
    return r

def rozw(A:int, B:int):
    print(gen(A-1, B, 1))

rozw(2,3)

