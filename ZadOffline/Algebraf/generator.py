import random

def generate_test_case():
    # 1. Zdefiniuj litery i stwórz losowe mapowanie na cyfry 1-9
    letters = list("ABCDEFGHI")
    digits = list(range(1, 10))
    random.shuffle(digits)
    
    key = {letters[i]: digits[i] for i in range(len(letters))}
    inv_key = {digits[i]: letters[i] for i in range(len(letters))}

    # 2. Wygeneruj N równań (np. od 3 do 8, aby test był sensowny)
    N = random.randint(3, 8)
    equations_to_print = []
    all_used_letters = set()
    
    generated_count = 0
    while generated_count < N:
        # 3. Twórz liczby, aż znajdziesz sumę bez '0'
        num1 = random.randint(1, 999)
        num2 = random.randint(1, 999)
        num3 = num1 + num2
        
        s_num1 = str(num1)
        s_num2 = str(num2)
        s_num3 = str(num3)
        
        # Odrzuć, jeśli '0' jest obecne (zgodnie z zasadami zadania)
        if '0' in (s_num1 + s_num2 + s_num3):
            continue
            
        # 4. Przekonwertuj liczby z powrotem na litery
        try:
            str1 = "".join([inv_key[int(d)] for d in s_num1])
            str2 = "".join([inv_key[int(d)] for d in s_num2])
            str3 = "".join([inv_key[int(d)] for d in s_num3])
        except KeyError:
            # To się zdarzy, jeśli liczba miała więcej niż 9 unikalnych cyfr
            # (niemożliwe z cyframi 1-9) lub jeśli nasze liczby są za duże
            continue

        # Zapisz równanie i użyte litery
        equations_to_print.append(f"{str1}+{str2}={str3}")
        all_used_letters.update(str1)
        all_used_letters.update(str2)
        all_used_letters.update(str3)
        generated_count += 1

    # 5. Oblicz oczekiwany wynik
    # (posortowane litery, które faktycznie wystąpiły)
    sorted_used_letters = sorted(list(all_used_letters))
    expected_solution = "".join([str(key[L]) for L in sorted_used_letters])

    # 6. Wydrukuj oczekiwany wynik i dane wejściowe
    # Linia 1: Oczekiwany wynik
    print(expected_solution)
    # Linia 2: N
    print(len(equations_to_print))
    # Reszta: Równania
    for eq in equations_to_print:
        print(eq)

if __name__ == "__main__":
    generate_test_case()
