'''
Zadanie 103.
 Dane są dwie tablice mogące pomieścić taką samą liczbę elementów: T1[N][N] i T2[M],
gdzie M=N*N. W każdym wierszu tablicy T1 znajdują się uporządkowane rosnąco (w obrębie wiersza)
liczby naturalne. Proszę napisać funkcję przepisującą wszystkie singletony (liczby występujące dokładnie
raz) z tablicy T1 do T2, tak aby liczby w tablicy T2 były uporządkowane rosnąco. Pozostałe elementy
tablicy T2 powinny zawierać zera.
'''

def res(T1, T2):
    N = len(T1)
    ind = [0 for _ in range(N)]
    i = -1

    while True:
        i += 1

        best_k = 0
        while best_k < N <= ind[best_k]:
            best_k += 1
        if best_k == N: break

        for k in range(N):
            if ind[k] < N and T1[k][ ind[k] ] < T1[best_k][ ind[best_k] ]:
                best_k = k

        if i > 0 and T2[i-1] == T1[best_k][ ind[best_k] ]:
            i -= 1
        else:
            T2[i] = T1[best_k][ ind[best_k] ]

        ind[best_k] += 1

T1 = [
    [1,1,2],
    [5,5,6],
    [8,9,10],
]
T2 = [0 for _ in range(10)]
res(T1, T2)
print(T2)