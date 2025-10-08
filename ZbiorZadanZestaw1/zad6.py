N = int(input(":"))

i = 1
sq = 0
sum = 0
while sum <= N:
    sum += i
    sq += 1
    i += 2
print(sq - 1)