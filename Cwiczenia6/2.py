"""
Zadanie 93. Dana jest liczba naturalna o niepowtarzających się cyfrach pośród których nie ma zera. Ile
różnych liczb podzielnych np. przez 7 można otrzymać poprzez wykreślenie dowolnych cyfr w tej liczbie. Np.
dla 2315 będą to 21, 35, 231, 315.
"""

def liczpodz(num: int, dziel: int = 7) -> int:
    maxMask = 1
    t = num
    l = 0
    while t > 0:
        maxMask *= 2
        l += 1
        t //= 10

    maxMask -= 1
    mask = 1
    s = 0
    while mask != maxMask:
        t = 0
        num1 = num
        p = 1
        for i in range(l):
            if mask & (1 << i):
                t += p * (num1 % 10)
                p *= 10
            num1 //= 10

        if t % dziel == 0: s += 1

        mask += 1
    return s

n = 2315
print(liczpodz(n))