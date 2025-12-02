from functools import cache
'''
Zadanie 161. 
Wyrazy budowane są z liter a..z. Dwa wyrazy ”ważą” tyle samo jeżeli: mają tę samą
liczbę samogłosek oraz sumy kodów ascii liter z których są zbudowane są identyczne, na przykład ′′ula′′ →
117, 108, 97 oraz ′′exe′′ → 101, 120, 101. Proszę napisać funkcję wyraz(s1,s2), która sprawdza czy jest możliwe
zbudowanie wyrazu z podzbioru liter zawartych w s2 ważącego tyle co wyraz s1. Dodatkowo funkcja powinna
wypisać znaleziony wyraz.
'''

@cache
def wyraz(s1, s2, w='') -> bool:
    if len(w) == len(s1):
        if sum([ord(l) for l in s1]) == sum([ord(l) for l in w]):
            if sum([1 for i in s1 if i in "aeiouy"]) == sum([1 for i in w if i in "aeiouy"]):
                return True
        return False

    for i in range(len(s2)):
        x = wyraz(s1, s2[:i] + s2[i+1:], w + str(s2[i]))
        if x: return True
    return False

print(wyraz("ula", "xxeet"))
