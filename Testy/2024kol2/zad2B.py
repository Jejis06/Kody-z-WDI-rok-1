def is_prime(x) -> bool:
    if x < 2: return False
    if x == 2: return True
    if x % 2 ==0: return False
    i = 3
    while i*i <= x:
        if x % i == 0: return False
        i += 2
    return True

def A(x: int) -> int:
    y = 0
    while x > 0:
        r = x % 10
        y = y*10 + r
        x //= 10
    return y + 1

def B(x) -> int:
    max_N = int(1e6) + 1
    for i in range(x+1, max_N):
        if is_prime(i):
            return i
    return -1


def C(x) -> int:
    if x == 0: return 0

    numerator = 1
    while numerator < x:
        numerator *= 10
    res = 0
    for _ in range(3):
        digit = numerator // x
        res = res* 10 + digit
        numerator = (numerator % x) * 10
    return res


optimal_path =""
def reqr(x,curr, path="", steps=0) -> None:
    global optimal_path
    if steps > 9: 
        return
    if curr == x:
        if len(optimal_path) > len(path):
            optimal_path = path
        elif optimal_path == "":
            optimal_path = path
        return

    reqr(x, A(curr), path + 'A', steps+1)
    reqr(x, B(curr), path + 'B', steps+1)
    reqr(x, C(curr), path + 'C', steps+1)


def cykl(x) -> str:
    global optimal_path
    optimal_path = ""
    reqr(x, A(x), 'A', 1)
    reqr(x, B(x), 'B', 1)
    reqr(x, C(x), 'C', 1)
    return optimal_path

print(cykl(3))
print(cykl(35))
print(cykl(45))
print(cykl(51))



