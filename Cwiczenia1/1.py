# ciag fibbonaciego do 1e6
# na jedna zmienna
a = 1; b = 1
while a < int(1e6):
    print(a)
    a,b = b, a+b
'''
from math import log, e

def ln(x):
    #return log(x)/log(e)
    return log(x, e)
def x_x(x):
    return x**x
def pochodna_x_x(x0):
    h = 1e-12
    return (x_x(x0 + h) - x_x(x0))/h
def pochodna_x_x_wzor(x0):
    return x_x(x0) + x_x(x0) * ln(x0)


print("aproksymacja wzoru na pochodna")
for i in range(1, 10):
    print(pochodna_x_x(i), end=' ')
print()
print("wzor na pochodna")
for i in range(1, 10):
    print(pochodna_x_x_wzor(i), end=' ')


print()
print("wzor na pochodna - aproksymacja wzoru na pochodna")
for i in range(1, 10):
    print(pochodna_x_x_wzor(i) - pochodna_x_x(i), end=' ')
'''
