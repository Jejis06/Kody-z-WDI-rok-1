from random import randint

def makeNewMatrix(T:list[list[int]], kolumna: int) -> list[list[int]]:
    new_size = len(T) - 1
    org_size = len(T)
    new_matrix = [[0 for _ in range(new_size)] for _ in range(new_size)] 

    ind_w = 0
    ind_k = 0
    for w in range(1, org_size):
        ind_k = 0
        for k in range(0, org_size):
            if k != kolumna: 
                new_matrix[ind_w][ind_k] = T[w][k]
                ind_k += 1
        ind_w += 1

    return new_matrix


def det(T: list[list[int]]) -> int:
    n = len(T)

    if n == 1: return T[0][0]
    suma = 0
    znak = 1
    for kol in range(0, n):
        T1 = makeNewMatrix(T, kol)
        suma += znak * T[0][kol] * det(T1)
        znak *= -1
    return suma

def gen_matrix(n:int) -> list[list[int]]:
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            matrix[i][j] = randint(1, 10)
    return matrix

def print_matrix(matrix):
    N = len(matrix)

    for i in range(N):
        for j in range(N):
            print(f"{matrix[i][j]:4}", end=' ')
        print()

mat = gen_matrix(3)
print_matrix(mat)
print(det(mat))


