from random import randint
n = randint(1, 100)
arr = []
spaces = [] 
for i in range(n):
    arr.append(randint(0, 10))
    spaces.append(randint(0,1))

print(n)
for i in range(n):
    if spaces[i]:
        print(arr[i], end='  ')
    else:
        print(arr[i], end=' ')


