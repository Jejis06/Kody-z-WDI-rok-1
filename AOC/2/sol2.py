

def check_pat(l) -> bool:
    first = l[0]
    for i in l:
        if first != i:
            return False
    return True

def split_chunks(l, cs) -> list[str]:
    return [l[i:i+cs] for i in range(0, len(l), cs)]

def checkNum(x:int) -> bool: 
    x_str = str(x)
    n = len(x_str)

    if n == 1: return False

    for i in range(2, n // 2 + 1):
        if n % i == 0:
            if check_pat(split_chunks(x_str, n//i)):
                return True
    return check_pat(split_chunks(x_str, 1))

raw = input()
ranges = [tuple(x.split('-')) for x in raw.split(',')]



res = 0
for r in ranges:
    for i in range(int( r[0] ), int( r[1] ) + 1):
        if checkNum(i):
            res += i
print(res)

