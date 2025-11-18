def is_prime(n):
    if n <= 1:  return False
    if n <= 3:  return True
    if n % 2 == 0 or n % 3 == 0:    return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:  return False
        i += 6
    return True


def differentDigits(n):
    return len(list(n)) == len(set(n))


def find(N, indeks = 0):
    if indeks >= len(N):    return 0

    minLocal = float('inf')

    max_length = len(N) - indeks
    for size in range(1, max_length + 1):
        digit = N[indeks:indeks + size]

        if differentDigits(digit) and is_prime(int(digit)):
            result = find(N, indeks + size)

            if result != float('inf'):
                finalResult = result + 1
                if finalResult < minLocal:
                    minLocal = finalResult

    return minLocal


def main_function(N):
    minGlobal = float('inf')
    indeks = 0

    for size in range(1, len(N) - 1):
        digit = N[indeks:indeks + size]

        if differentDigits(digit) and is_prime(int(digit)):
            result = find(N, indeks + size)

            if result != float('inf'):
                finalResult = result + 1
                if finalResult < minGlobal:
                    minGlobal = finalResult

    if minGlobal == float('inf'):
        return "BRAK"
    return minGlobal


N = input("").strip()
print(main_function(N))
