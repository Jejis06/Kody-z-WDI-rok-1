import sys

N = int(input(":"))
sum = 0
a = 1
b = 1
while sum < N:
    sum += a
    a, b = b, a+b

if sum == N:
    print("YES")
    sys.exit(0)
if sum > N:
    a = 1
    b = 1
    while sum > N:
        sum -= a
        a, b = b, a+b
    if sum == N:
        print("YES")
        sys.exit(0)
print("NO")

