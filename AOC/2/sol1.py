

def checkNum(x:int) -> bool: 
    x_str = str(x)
    n = len(x_str)

    return (n % 2 == 0) and (x_str[:n//2] == x_str[n//2:])
    

raw = input()
ranges = [tuple(x.split('-')) for x in raw.split(',')]

res = 0
for r in ranges:
    for i in range(int( r[0] ), int( r[1] ) + 1):
        if checkNum(i):
            res += i
print(res)
