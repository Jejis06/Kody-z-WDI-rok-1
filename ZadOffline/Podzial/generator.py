import random
import sys

# ==========================================
# 1. SOLVER (Algorytm DP do obliczania wyniku)
# ==========================================

def is_prime(n):
    if n < 2: return False
    if n == 2: return True
    if n % 2 == 0: return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0: return False
    return True

def unique_nums(s):
    if len(s) > 10: return False
    return len(set(s)) == len(s)

def solve_dp(digits):
    """Rozwiązuje zadanie metodą DP, aby uzyskać poprawny Expected Output"""
    # Usuwamy spacje do obliczeń (algorytm działa na czystych cyfrach)
    clean_digits = digits.replace(" ", "")
    N = len(clean_digits)
    
    if N == 0: return "BRAK"
    
    INF = 10**9
    dp = [INF] * (N + 1)
    dp[0] = 0
    
    for i in range(1, N + 1):
        max_len = min(10, i)
        for length in range(1, max_len + 1):
            j = i - length
            
            if i == N and j == 0:
                continue
                
            sub = clean_digits[j:i]
            if not unique_nums(sub): continue
            
            try:
                if is_prime(int(sub)):
                    if dp[j] != INF:
                        dp[i] = min(dp[i], dp[j] + 1)
            except ValueError:
                continue

    if dp[N] == INF:
        return "BRAK"
    return str(dp[N])

# ==========================================
# 2. GENERATOR
# ==========================================

def inject_whitespace(s):
    """Wstawia LOSOWE SPACJE do ciągu cyfr."""
    res = []
    # Zmiana: Tylko spacje są dozwolone
    whitespace_chars = [' ', '  ', '   '] 
    
    for char in s:
        res.append(char)
        # 20% szansy na wstawienie spacji po cyfrze
        if random.random() < 0.20:
            res.append(random.choice(whitespace_chars))
            
    return "".join(res)

def generate_test_case(idx, category, length_range):
    # Losowanie długości N
    n = random.randint(length_range[0], length_range[1])
    
    # Generowanie ciągu cyfr
    digits = "".join([str(random.randint(1, 9))] + [str(random.randint(0, 9)) for _ in range(n - 1)])
    
    # Psucie wejścia (dodawanie SPACJI)
    dirty_input = inject_whitespace(digits)
    
    # Obliczanie poprawnego wyniku (na podstawie ciągu ze spacjami, solver sobie je usunie)
    expected_output = solve_dp(dirty_input)
    
    # Formatowanie Bash
    print(f"\n# --- Test OFF {idx} ({category} N={n}) ---")
    print(f'tests_name+=("Test OFF {idx} [{category}]")')
    print(f'tests_input+=("{dirty_input}")')
    print(f'tests_output+=("{expected_output}")')
    
    # Zmiana: Użycie zmiennej bashowej jako stringa
    print('tests_points+=($offpoints)')

def main():
    # Pobieranie liczby testów od użytkownika (interaktywnie lub domyślnie)
    try:
        # Sprawdzamy czy podano argument przy uruchomieniu, jak nie to pytamy
        if len(sys.argv) > 1:
            total_tests = int(sys.argv[1])
        else:
            sys.stderr.write("Podaj liczbę testów do wygenerowania: ")
            sys.stderr.flush()
            line = sys.stdin.readline()
            if not line:
                total_tests = 10
            else:
                total_tests = int(line.strip())
    except ValueError:
        total_tests = 10

    # Podział na grupy
    small_count = total_tests // 3
    medium_count = total_tests // 3
    large_count = total_tests - small_count - medium_count
    
    current_idx = 1
    
    print("\n# ==========================================")
    print("# GENERATED TESTS START")
    print("# ==========================================")

    # 1. MAŁE (9 <= N <= 33)
    for _ in range(small_count):
        generate_test_case(current_idx, "SMALL", (9, 33))
        current_idx += 1
        
    # 2. ŚREDNIE (34 <= N <= 66)
    for _ in range(medium_count):
        generate_test_case(current_idx, "MEDIUM", (34, 66))
        current_idx += 1

    # 3. DUŻE (67 <= N <= 99)
    for _ in range(large_count):
        generate_test_case(current_idx, "LARGE", (67, 99))
        current_idx += 1

    print("\n# ==========================================")
    print("# GENERATED TESTS END")
    print("# ==========================================")

if __name__ == "__main__":
    main()
