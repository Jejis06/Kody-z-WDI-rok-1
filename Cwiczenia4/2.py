_ = '''
Zadanie 98. Dana jest tablica T[N][N]. Proszę napisać funkcję wypełniającą tablicę kolejnymi liczbami
naturalnymi po spirali.
'''

N = 11
arr = [[0 for i in range(N)] for i in range(N)]

#d [wiersz] [kolumna]

def spiral(arr) -> int:
    N = len(arr)
    a = 0
    b = N- 1
    k = 1
    while a < b:
        # zredukowac do jednej petli
        for i in range(a, b): arr[a][i] = k; k += 1
        for i in range(a, b): arr[i][b] = k; k += 1
        for i in range(b, a, -1): arr[b][i] = k; k += 1
        for i in range(b, a, -1): arr[i][a] = k; k += 1

        a += 1; b -= 1
    if N % 2 >= 1: arr[a][b] = k
    return k



def advance_col(rgb):
    rgb[0] += 1
    rgb[1] += 1
    rgb[2] += 1


def format_col(num, avglen, rgb) -> str:
    t = str(num)
    while len(t) < avglen:
        t = ' ' + t

    r, g, b = rgb
    advance_col(rgb)
    return (f"\033[38;2;{r};{g};{b}m{t}\033[0m")


def process_spiral(arr, avglen):
    N = len(arr)
    a = 0; b = N- 1

    rgb = [40,11,32]
    while a < b:
        # zredukowac do jednej petli
        for i in range(a, b): arr[a][i] = format_col(arr[a][i], avglen, rgb)
        for i in range(a, b): arr[i][b] = format_col(arr[i][b], avglen, rgb)
        for i in range(b, a, -1): arr[b][i] = format_col(arr[b][i], avglen, rgb)
        for i in range(b, a, -1): arr[i][a] = format_col(arr[i][a], avglen, rgb)

        a += 1; b -= 1
    if N % 2 >= 1: arr[a][b] = format_col(arr[a][b], avglen, rgb)



maxk = spiral(arr)
avglen = len(str(maxk))


process_spiral(arr, avglen)

for i in range(N):
    for j in range(N):
        print(arr[i][j], end=' ')
    print()

