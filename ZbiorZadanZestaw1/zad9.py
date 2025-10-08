# [4,5]
# f(x) = x^x - 2025
a = 4
b = 5
eps = 1e-6

def f(x):
    return pow(x,x) - 2025

while abs(a - b) >= eps:
    print(a,b, a-b)
    x1 = (a + b)/2
    if abs(f(x1)) <= eps:
        break
    elif f(x1) * f(a) < 0:
        b = x1
    else:
        a = x1
print((a + b) / 2)