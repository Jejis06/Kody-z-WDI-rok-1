
def sumDziel(n):
    if n <= 1: return 0
    i = 2
    sum = 1
    while i <= n/2:
        if n % i == 0:
            sum += i
        i += 1
    return sum

for i in range(1, int(1e6)):
    if i == sumDziel(i):
        print(i)
