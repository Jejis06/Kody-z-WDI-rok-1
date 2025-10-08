from math import sqrt
s = float(input(":"))
a = 1
diff = 2
eps = 1e-6

while abs(diff) > eps:
    diff = -a
    a = (s/a + a)/2
    diff += a

print(a)