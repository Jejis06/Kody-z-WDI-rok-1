from time import sleep
from os import system
from sys import stdout

# w,k
T = [[0 for _ in range(5)] for _ in range(5)]

def in_bounds(w, k, n) -> bool:
    if w >= n: return False
    if w < 0: return False
    if k >= n: return False
    if k < 0: return False

    return True

def write(T):
    s = ""
    for row in T:
        s += (''.join([f'{kol:4}' for kol in row])) + '\n'
    return s

# skoczek - 1
def rozmieszczenie(T:list[list[int]], w:int=0, k:int=0, r:int=1) -> None:
    n = len(T)

    T[w][k] = r
    if r == n*n:
        print(write(T))
        exit(0)

    moves = [ (2, -1), (2, 1), (-2, -1), (-2, 1), (1, 2), (1, -2), (-1, 2), (-1, -2), ]
    for move in moves:
        if in_bounds(w+move[0], k+move[1], n) and T[w+move[0]][k + move[1]] == 0:
            rozmieszczenie(T, w+move[0], k+move[1], r+1)
    T[w][k] = 0

rozmieszczenie(T)
