# ciag fibbonaciego do 1e6
# na jedna zmienna
a = 1; b = 1
while a < int(1e6):
    print(a)
    a,b = b, a+b
