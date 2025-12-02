from functools import cache

'''
Zad 158
Napisać program wypisujący wszystkie możliwe podziały liczby naturalnej na 
sumę składników. Na przykład dla liczby 4 są to: 1+3, 1+1+2, 1+1+1+1, 2+2.
'''

@cache
def podz(n: int, w:str='',j:int=1) -> None:
    if n == 0:
        if len(w.split('+')) == 1: return
        print(w)
        return 
    for i in range(j, n+1):
        wyr = str(i) if w == '' else f" + {i}"
        podz(n-i, w + wyr, i)


podz(4)
