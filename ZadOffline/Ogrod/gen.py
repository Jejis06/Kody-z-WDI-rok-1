import sys
import random

# --- KONFIGURACJA GENERATORA ---
MIN_N = 200       # Minimalny bok ogrodu
MAX_N = 200      # Maksymalny bok ogrodu (dla czytelności, zadanie dopuszcza 100)
EXTRA_MIRRORS_PERCENT = 0.99 # Jaki % wolnych pól wypełnić losowymi lustrami (szum)

# Kierunki: 0:N, 1:E, 2:S, 3:W
DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def get_reflection_angle(d_in, d_out):
    """
    Zwraca kąt lustra potrzebny do zmiany kierunku z d_in na d_out.
    Zwraca None, jeśli taka zmiana jest niemożliwa jednym lustrem.
    """
    # 45 stopni (/): N<->E (0<->1), S<->W (2<->3)
    map_45 = {0: 1, 1: 0, 2: 3, 3: 2}
    if map_45.get(d_in) == d_out:
        return 45
    
    # 135 stopni (\): N<->W (0<->3), S<->E (2<->1)
    map_135 = {0: 3, 3: 0, 2: 1, 1: 2}
    if map_135.get(d_in) == d_out:
        return 135
        
    return None

def simulate_beam(N, start_pos, start_dir, mirrors):
    """
    Symuluje wiązkę światła i zwraca zbiór odwiedzonych pól.
    Potrzebne do weryfikacji, czy przestawione lustro jest ukryte.
    """
    visited = set()
    r, c = start_pos
    d = start_dir
    steps = 0
    max_steps = 4 * N * N # Zabezpieczenie przed pętlą
    
    while 0 <= r < N and 0 <= c < N and steps < max_steps:
        visited.add((r, c))
        steps += 1
        
        if (r, c) in mirrors:
            angle = mirrors[(r, c)]
            # Odbicie
            if angle == 45:
                mapping = {0: 1, 1: 0, 2: 3, 3: 2}
                d = mapping[d]
            else:
                mapping = {0: 3, 3: 0, 2: 1, 1: 2}
                d = mapping[d]
        
        dr, dc = DIRS[d]
        r += dr
        c += dc
        
    return visited

def generate_test_case():
    N = random.randint(MIN_N, MAX_N)
    
    # 1. Generowanie poprawnej ścieżki (Randomized DFS)
    # Startujemy w (0,0) wchodząc z Północy (czyli kierujemy się na Południe - 2)
    # Cel: (N-1, N-1), wyjście na Południe (2)
    
    path_mirrors = {} # (r, c) -> angle
    path_cells = set() # (r, c)
    
    stack = [(0, 0, 2, {}, set())] # r, c, dir_in, current_mirrors, visited
    
    solution_mirrors = None
    
    # Prosty randomized DFS do znalezienia ścieżki
    attempts = 0
    while attempts < 1000:
        attempts += 1
        
        # Resetujemy do startu co próbę, żeby nie robić backtrackingu w nieskończoność
        # (Szybciej jest wylosować nową ścieżkę od zera niż cofać się głęboko)
        curr_r, curr_c = 0, 0
        curr_d = 2 # Ruch w dół
        curr_mirrors = {}
        curr_visited = set([(0,0)])
        path_found = False
        
        step_limit = N * N 
        steps = 0
        
        while steps < step_limit:
            steps += 1
            
            # Czy dotarliśmy do końca?
            if curr_r == N-1 and curr_c == N-1:
                # Musimy wyjść na południe.
                if curr_d == 2:
                    path_found = True
                    break
                # Jeśli jesteśmy na końcu ale zły kierunek, musimy postawić lustro
                req_angle = get_reflection_angle(curr_d, 2)
                if req_angle:
                    curr_mirrors[(curr_r, curr_c)] = req_angle
                    path_found = True
                    break
            
            # Decyzja: idź prosto albo skręć
            # Preferujemy ruch w stronę celu (N-1, N-1)
            candidates = []
            
            # Opcja 1: Prosto
            dr, dc = DIRS[curr_d]
            nr, nc = curr_r + dr, curr_c + dc
            if 0 <= nr < N and 0 <= nc < N and (nr, nc) not in curr_visited:
                dist = abs((N-1)-nr) + abs((N-1)-nc)
                candidates.append((nr, nc, curr_d, None, dist)) # None = brak lustra
                
            # Opcja 2 i 3: Skręt (wymaga lustra)
            possible_turns = []
            if curr_d in [0, 2]: possible_turns = [1, 3] # N/S -> E/W
            else: possible_turns = [0, 2] # E/W -> N/S
            
            for next_d in possible_turns:
                angle = get_reflection_angle(curr_d, next_d)
                dr, dc = DIRS[next_d]
                nr, nc = curr_r + dr, curr_c + dc
                if 0 <= nr < N and 0 <= nc < N and (nr, nc) not in curr_visited:
                     dist = abs((N-1)-nr) + abs((N-1)-nc)
                     candidates.append((nr, nc, next_d, angle, dist + 2)) # +2 kara za zakręt (chcemy prostsze ścieżki)
            
            if not candidates:
                break # Ślepa uliczka
            
            # Sortuj po dystansie do celu + losowość
            candidates.sort(key=lambda x: x[4] + random.uniform(0, 5))
            
            # Wybierz najlepszego kandydata
            next_r, next_c, next_d, angle, _ = candidates[0]
            
            if angle:
                curr_mirrors[(curr_r, curr_c)] = angle
                
            curr_visited.add((next_r, next_c))
            curr_r, curr_c = next_r, next_c
            curr_d = next_d
            
        if path_found:
            solution_mirrors = curr_mirrors
            path_cells = curr_visited
            break
    
    if solution_mirrors is None:
        # Fallback if generation fails
        return generate_test_case()

    # 2. Dodanie szumu (losowe lustra poza ścieżką)
    final_mirrors = solution_mirrors.copy()
    all_cells = [(r, c) for r in range(N) for c in range(N)]
    random.shuffle(all_cells)
    
    for r, c in all_cells:
        if (r, c) not in path_cells and random.random() < EXTRA_MIRRORS_PERCENT:
            final_mirrors[(r, c)] = random.choice([45, 135])

    # 3. Sabotaż: Wybierz lustro ze ścieżki do przesunięcia
    # Musi to być lustro, które po usunięciu przerywa połączenie
    if not solution_mirrors:
        # Jeśli ścieżka jest prosta bez luster (np. linia w dół), dodajmy chociaż jedno lustro dummy i je przesuńmy
        # Ale w tym zadaniu to rzadkość przy DFS. Restart.
        return generate_test_case()
        
    correct_pos = random.choice(list(solution_mirrors.keys()))
    correct_angle = solution_mirrors[correct_pos]
    del final_mirrors[correct_pos] # Usuwamy ze ścieżki
    
    # 4. Znajdź "Złe miejsce" (gdzie przestawić lustro)
    # Warunek: Miejsce musi być puste ORAZ po wstawieniu tam lustra
    # nie może ono być odwiedzone przez wiązkę ze startu ani od tyłu z końca.
    
    # Symulacja na planszy BEZ tego lustra, żeby zobaczyć gdzie dociera światło
    visited_from_start = simulate_beam(N, (0,0), 2, final_mirrors)
    visited_from_end = simulate_beam(N, (N-1, N-1), 0, final_mirrors) # 0 = Północ (pod prąd)
    
    bad_pos = None
    random.shuffle(all_cells)
    
    for r, c in all_cells:
        # Musi być puste (nie ma tam innego lustra)
        if (r, c) not in final_mirrors:
            # I nie może leżeć na trasie uszkodzonej wiązki
            if (r, c) not in visited_from_start and (r, c) not in visited_from_end:
                bad_pos = (r, c)
                break
    
    if bad_pos is None:
        return generate_test_case() # Nie znaleziono bezpiecznego miejsca na ukrycie lustra
        
    # Wstawiamy lustro w złe miejsce (możemy zmienić kąt albo zostawić, zadanie mówi "nie wiemy czy zmienił kąt")
    final_mirrors[bad_pos] = random.choice([45, 135])
    
    # --- WYPISANIE WYNIKU ---
    print(f"{N} {len(final_mirrors)}")
    
    # Sortowanie dla estetyki (nie wymagane przez zadanie)
    sorted_locs = sorted(final_mirrors.keys())
    for r, c in sorted_locs:
        print(f"{r} {c} {final_mirrors[(r,c)]}")
        
    # Opcjonalnie: wypisz na stderr rozwiązanie dla weryfikacji
    sys.stderr.write(f"DEBUG: Rozwiązanie -> Zabierz z: {bad_pos}, Wstaw w: {correct_pos}\n")

if __name__ == "__main__":
    # Zwiększ limit rekurencji dla głębokich DFS
    sys.setrecursionlimit(2000)
    generate_test_case()
