from math import log2
def czy_5_pokr(a, b) -> bool:

    meeta = [False] * 5
    meetb = [False] * 5
    
    if a == 0: meeta[0] = True
    while a > 0:
        meeta[a % 5] = True
        a //= 5
    
    if b == 0: meetb[0] = True
    while b > 0:
        r = b % 5
        if meeta[r] == False: return False
        meetb[r] = True
        b //= 5
    return meeta == meetb 

def in_bounds(w:int, k:int, N:int) -> bool:
    return (0 <= w < N) and (0 <= k < N)

def lucky17(T) -> bool:
    N = len(T)

    luncky_nums_kols = [0] * N
    luncky_nums_rows = [0] * N


    for w in range(N):
        for k in range(N):
            val = T[w][k]
            cntr = 0

            for dw in range(-2, 3):
                for dk in range(-2, 3):
                    if dw == dk == 0: continue
                    nw, nk = w + dw, k+dk
                    if 0<=nw<N and 0<=nk<N and czy_5_pokr(val, T[nw][nk]):
                        cntr += 1
            if cntr == 17:
                luncky_nums_kols[k] += 1
                luncky_nums_rows[k] += 1
            if luncky_nums_rows[w] > 1 or luncky_nums_kols[k] > 1:
                return True


    return False


