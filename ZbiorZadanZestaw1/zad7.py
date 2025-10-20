# an = (S/an-1 + an-1)/2

a = 1
eps = 1e-6
diff = 1

S = float(input(":"))

while abs(diff) > eps:
    diff = -a
    a = (S/a + a) /2
    diff += a
print(a)

# a