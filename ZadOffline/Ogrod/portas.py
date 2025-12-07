import sys


def mozliwy_ruch(T, wiersz, kolumna):
    return 0 <= wiersz < len(T) and 0 <= kolumna < len(T)


def odbijanie_przez_lustro(T, pw, pk, aw, ak):
    """
    funkcja dostaje aktualne kordynaty, poprzednie kordyanty, kat lustra
    z poprzednich koordynatow wiemy w ktora strone odbija promien lustro
    funkcja zwraca koordynaty nastepnego ruchu
    """

    # wyznaczanie kierunku promienia (skad przyszedl)
    if pw < aw:
        kierunek = "DOWN"
    elif pw > aw:
        kierunek = "UP"
    elif pk < ak:
        kierunek = "RIGHT"
    else:
        kierunek = "LEFT"

    kat = T[aw][ak]
    if kat == 45:
        # wyznaczenie kierunku oraz wspolrzednych dla lustra 45 stopni
        if kierunek == "RIGHT":
            wiersz = aw - 1
            kolumna = ak
            if mozliwy_ruch(T, wiersz, kolumna): return wiersz, kolumna, "UP"
        elif kierunek == "DOWN":
            wiersz = aw
            kolumna = ak - 1
            if mozliwy_ruch(T, wiersz, kolumna): return wiersz, kolumna, "LEFT"
        elif kierunek == "LEFT":
            wiersz = aw + 1
            kolumna = ak
            if mozliwy_ruch(T, wiersz, kolumna): return wiersz, kolumna, "DOWN"
        else:
            wiersz = aw
            kolumna = ak + 1
            if mozliwy_ruch(T, wiersz, kolumna): return wiersz, kolumna, "RIGHT"
    else:
        # wyznaczenie kierunku oraz wspolrzednych dla lustra 135 stopni
        if kierunek == "RIGHT":
            wiersz = aw + 1
            kolumna = ak
            if mozliwy_ruch(T, wiersz, kolumna): return wiersz, kolumna, "DOWN"
        elif kierunek == "DOWN":
            wiersz = aw
            kolumna = ak + 1
            if mozliwy_ruch(T, wiersz, kolumna): return wiersz, kolumna, "RIGHT"
        elif kierunek == "LEFT":
            wiersz = aw - 1
            kolumna = ak
            if mozliwy_ruch(T, wiersz, kolumna): return wiersz, kolumna, "UP"
        else:
            wiersz = aw
            kolumna = ak - 1
            if mozliwy_ruch(T, wiersz, kolumna): return wiersz, kolumna, "LEFT"

    return -1, -1, "error"


def sciezka(T, wiersz, kolumna, direction):
    tablica = []
    N = len(T)
    indeks = 0

    # Zabezpieczenie pętli (N*N to może być za mało dla skomplikowanych odbić, ale wklejam jak było)
    while indeks <= N * N * 4:
        if mozliwy_ruch(T, wiersz, kolumna):
            tablica.append((wiersz, kolumna))
            if T[wiersz][kolumna] == 0:
                if direction == "DOWN":
                    wiersz += 1
                elif direction == "UP":
                    wiersz -= 1
                elif direction == "LEFT":
                    kolumna -= 1
                else:
                    kolumna += 1
            else:
                wiersz, kolumna, direction = odbijanie_przez_lustro(T, tablica[indeks - 1][0], tablica[indeks - 1][1],
                                                                    wiersz, kolumna)
                if direction == 'error':
                    return tablica
            indeks += 1
        else:
            return tablica
    return tablica


def znajdz_punkt_wspolny(start, meta):
    """
    szukanie punktu przeciecia sie tych dwoch tras
    ten punkt bedze tym gdzie trzeba umiescic lustro
    """
    for element in start:
        if element in meta:
            return element
    return -1, -1


def znajdz_nieuzywane_lustro(T, sciezka1, sciezka2):
    for element in sciezka1:
        r, c = element[0], element[1]
        T[r][c] = 0
    for element in sciezka2:
        r, c = element[0], element[1]
        T[r][c] = 0

    for i in range(len(T)):
        for j in range(len(T[i])):
            if T[i][j] == 45 or T[i][j] == 135:
                return i, j
    return -1, -1


def main_function(T):
    n = len(T)

    # przeanalizowac sciezke promienia od lewej gory
    trasaStart = sciezka(T, 0, 0, "DOWN")

    # przeanalizowac sciezke promienia od prawego dolu
    trasaKoniec = sciezka(T, n - 1, n - 1, "UP")

    # to jest miejsce gdzie dwie sciezki sie krzyzuja
    # wiec jest to rowniez miejsce gdzie trzeba postawic lustro
    wierszSzukany, kolumnaSzukana = znajdz_punkt_wspolny(trasaStart, trasaKoniec)

    # zlokalizowanie lustra ktore jest niewykorzystywane i to je trzeba przestawic
    bezuzyteczne = znajdz_nieuzywane_lustro(T, trasaStart, trasaKoniec)
    wierszNieuzywany = bezuzyteczne[0]
    kolumnaNieuzywana = bezuzyteczne[1]

    print(f"{wierszNieuzywany} {kolumnaNieuzywana}")
    print(f"{wierszSzukany} {kolumnaSzukana}")


# Wczytywanie danych
line1 = sys.stdin.readline().split()
if line1:
    N = int(line1[0])
    L = int(line1[1])
    land = [[0 for _ in range(N)] for _ in range(N)]
    for _ in range(L):
        line = sys.stdin.readline()
        if line:
            coordinates = list(map(int, line.strip().split()))
            land[coordinates[0]][coordinates[1]] = coordinates[2]

    main_function(land)
