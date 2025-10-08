
minA = 2024
minB = 1
A = 1
B = 1

for A in range(1, 2025):
    for B in range(1, 2025):
        a = A
        b = B
        print(a,b)
        while a <= 2025:
           a,b = b,a+b
        if a == 2025 and a + b < minA + minB:
                minA = a
                minB = b
                break

print(minA, minB)

