from math import gcd
from random import randint

def sumOfdig(num):
    sum = 0
    while (num != 0):
        sum += num % 10
        num = num // 10
    return sum

# male twierdzenie fermata
def check_prime(p, n=100):
    if p<2: return False
    if p == 2 or p == 3: return True
    if p % 2 == 0: return False
    for i in range(n):
        a = randint(2, p-1)
        if gcd(a, p) != 1: return False
        if pow(a, p-1, p) != 1: return False
    return True

# rekurencyjne generowanie ciagow nierosnacych
def gen_nonincreasing(length, max_digit=9):
    if length == 0:
        yield ()
    else:
        for d in range(max_digit, -1, -1):  # od max_digit do 0
            for suffix in gen_nonincreasing(length - 1, d):
                yield (d,) + suffix

def search_combs(n):
    nums = []
    # generujemy wszystkie kombinacje ciagow nierosnacych o dlugosci i
    for seq in gen_nonincreasing(n):
        num = int(''.join(map(str, seq)))
        nums.append(num)

    nums.pop(len(nums) - 1)

    # wygenerowane liczby sa ulozone od najwiekszej do najmniejszej wiec iterujemy sie po ich tablicy od konca
    for i in range(len(nums)-1, -1, -1):
        num = nums[i]
        print(num)
        if check_prime(num) and (sumOfdig(num) == 101):
            return num
    return None



def main():
    # ciag to kolejne cyfry danej liczby l
    # najmniejszy mozliwy ciag dla ktorego suma cyfr to 101 to ciag skladajacy sie z samych 9 o dlugosci ceil(101/9) = 12
    # suma cyfr takiego ciagu jest rowna 108 ze wzgledu na zaokraglenie w gore wiec istnieje szansa ze ktorys z takich ciagow tworzy
    # liczbe pierwsza o sumie 101 dlatego sprawdzamy ciagi >= 12
    # zeby nie sprawdzac wszystkich ciagow od razu generujemy jedynie ciagi w ktorych cyfry sa ulozone nierosnaco bo jest ich dla dlugosci 12 ok. 250 000 a dla dlugosci 13 - 497 419
    # takich ciagow jest malo w porownaniu do wszystkich mozliwych ciagow ktorych jest az (10^12 + 10^13 - ciagi z zerami)
    # Pozostaje tylko idac od najmniejszej liczby sprawdzic ktora z nich jest pierwsza oraz sumuje sie do 101 i numer jest znaleziony


    # patrzac na zlozonosc dla rozwazanaego ciagu dlugosci l normalnie musielibysmy sprawdzic 10^l mozliwosci
    # natomiast w tym rozwiazaniu udaje nam sie to zrobic w (l + 10 - 1 nad l) [symbol newtona]
    for i in range(12, 20):
        print(f"Searching combinations of length {i}:")
        combs = search_combs(i)
        if combs is not None:
            print(f"Found smallest number fitting restrictions: {combs}")
            break
        else: print("Not found fitting given restrictions")

if __name__ == '__main__':
    main()