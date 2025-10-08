# Szykanie wszystkich dzielnikow N

N = int(input(":"))

i = 1
while i <= N//2:
    if N % i == 0:
        print(i)
    i += 1
print(N)
