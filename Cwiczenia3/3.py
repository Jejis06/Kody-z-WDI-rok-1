# zadanie 67

N = 1000
e = [0 for _ in range(N+1)]
w = [0 for _ in range(N+1)]

e[0] = w[0] = 1

m = 1

N = 1000

while sum(w) > 0:
    p = 0
    for i in range(N,-1, -1):
        e[i] = e[i] + w[i] + p
        p = e[i]//10
        e[i] = e[i] % 10

    m += 1

    #w =  w / m, dzielenie liczby
    r = 0
    for i in range(N+1):
        r = r * 10 + w[i]
        w[i] = r // m
        r = r % m


    '''  >>>>>>> dzielenie stringowe
    w1 = int(''.join(str(w[i]) for i in range(N+1)))
    m1 = m

    res = str(w1 // m1)
    w = [int(i) for i in res]
    if len(w) < len(e):
        w = [0] * (len(e)-len(w)) + w
    '''


print(e[0], end='.')
for i in e:
    print(i, end='')