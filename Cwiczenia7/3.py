'''
Zadanie 147. Szachownica jest reprezentowana przez tablicę T[8][8] wypełnioną liczbami naturalnymi
zawierającymi koszt przebywania na danym polu szachownicy. Król szachowy znajduje się w wierszu 0 i
kolumnie k. Król musi w dokładnie 7 ruchach dotrzeć do wiersza 7. Proszę napisać funkcję, która wyznaczy
minimalny koszt przejścia króla. Do funkcji należy przekazać tablicę t oraz startową kolumnę k. Koszt
przebywania na polu startowym i ostatnim także wliczamy do kosztu przejścia
'''

def koszt(T, w, k) -> int:
    if k < 0 or k > 7: return float('inf')
    if w == 7: return T[w][k]
    return T[w][k] + min(koszt(T, w+1, k), koszt(T, w+1, k+1), koszt(T, w+1, k-1))

minCost = None
def zadanie(T, k, r=0, sum=0) -> None:
    global minCost
    N = len(T)
    if r == 8:
        minCost = min(minCost, sum)
        return
    zadanie(T, k, r+1, sum+ T[r][k])
    if k < 7: zadanie(T, k+1, r+1, sum + T[r][k])
    if k > 0: zadanie(T, k-1, r+1, sum + T[r][k])

def solve(T, k) -> int:
    #global minCost
    #minCost = float('inf')
    #zadanie(T, k)
    #return minCost
    return koszt(T,0,k)
