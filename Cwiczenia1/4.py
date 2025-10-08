import sys
n = int(input(":"))
sum = 0
i = 1
a = 1
b = 1
while sum < n:
    sum += a
    a, b = b, a+b
    i+=1

if sum == n:
    print("TAK")
    sys.exit(0)

elif sum > n:
    a = 1
    b = 1
    while sum > n:
        sum -= a
        a, b = b, a + b
        i += 1

    if sum == n:
        print("TAK")
        sys.exit(0)
    else:
        print("NIE")
