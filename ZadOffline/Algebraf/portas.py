import re


def liczenie_wartosci_rownania(napis, wartosci):
    licznik = 0
    wynik = 0
    for i in range(len(napis) - 1, -1, -1):
        wynik += wartosci[ord(napis[i]) - 65] * 10 ** licznik
        licznik += 1
    return wynik


def sprawdzanie_rownan(rownanie, wartosci):
    s1 = rownanie[0]
    s2 = rownanie[1]
    s3 = rownanie[2]

    s1_value = liczenie_wartosci_rownania(s1, wartosci)
    s2_value = liczenie_wartosci_rownania(s2, wartosci)
    s3_value = liczenie_wartosci_rownania(s3, wartosci)

    if s1_value + s2_value == s3_value:
        return True
    return False


def zbior_liter(tablica_rownan):
    zbior = set()
    for rownanie in tablica_rownan:
        for element in rownanie:
            for litera in element:
                zbior.add(litera)
    return zbior


znalezione_rozwiazania = []


def solve(indeks_litery, tablica_rownan, wartosci_liter, cyfra_uzyta, max_indeks_litery):
    if indeks_litery == 9:

        wszystko_pasuje = True
        for rownanie in tablica_rownan:
            if not sprawdzanie_rownan(rownanie, wartosci_liter):
                wszystko_pasuje = False
                break

        if wszystko_pasuje:
            rozwiazanie = []
            for i in range(max_indeks_litery + 1):
                rozwiazanie.append(wartosci_liter[i])

            znalezione_rozwiazania.append(rozwiazanie)

        return

    if wartosci_liter[indeks_litery] == -1:
        solve(indeks_litery + 1, tablica_rownan, wartosci_liter, cyfra_uzyta, max_indeks_litery)
    else:
        for cyfra in range(1, 10):

            if not cyfra_uzyta[cyfra]:
                wartosci_liter[indeks_litery] = cyfra
                cyfra_uzyta[cyfra] = True

                solve(indeks_litery + 1, tablica_rownan, wartosci_liter, cyfra_uzyta, max_indeks_litery)

                cyfra_uzyta[cyfra] = False
                wartosci_liter[indeks_litery] = 0


def main_function(tablica_rownan):
    unikalne_litery = zbior_liter(tablica_rownan)

    max_indeks_litery = 0

    wartosci_liter = [-1 for _ in range(9)]
    for element in unikalne_litery:
        indeks = ord(element) - 65
        wartosci_liter[indeks] = 0
        if indeks > max_indeks_litery:
            max_indeks_litery = indeks

    cyfra_uzyta = [False] * 10

    solve(0, tablica_rownan, wartosci_liter, cyfra_uzyta, max_indeks_litery)

    if len(znalezione_rozwiazania) == 1:
        return "".join(map(str, znalezione_rozwiazania[0]))
    else:
        return "BRAK"


tablica_rownan = []
N = int(input(""))
for _ in range(N):
    napis = input("")
    tablica_rownan.append(re.split(r"[+=]", napis))

print(main_function(tablica_rownan))
