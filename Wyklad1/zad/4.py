from math import gcd
from random import randint

def sumOfdig(num):
    sum = 0
    while (num != 0):
        sum += num % 10
        num = num // 10
    return sum

def check_prime(p, n=100):
    if p<2: return False
    if p == 2 or p == 3: return True
    if p % 2 == 0: return False
    for i in range(n):
        a = randint(2, p-1)
        if gcd(a, p) != 1: return False
        if pow(a, p-1, p) != 1: return False
    return True

def gen_nonincreasing(length, max_digit=9):
    if length == 0:
        yield ()
    else:
        for d in range(max_digit, -1, -1):  # od max_digit do 0
            for suffix in gen_nonincreasing(length - 1, d):
                yield (d,) + suffix

def search_combs(n):
    nums = []
    for seq in gen_nonincreasing(n):
        num = int(''.join(map(str, seq)))
        nums.append(num)

    nums.pop(len(nums) - 1)

    for i in range(len(nums)-1, -1, -1):
        num = nums[i]
        print(num)
        if check_prime(num) and (sumOfdig(num) == 101):
            return num
    return None



def main():
    # najmniejszy mozliwy ciag dla ktorego suma cyfr to 101 to ciag skladajacy sie z samych 9 o dlugosci ceil(101/9) = 12
    # taki ciag nie jest liczba pierwsza bo dzieli sie przez 9 wiec najprawdopodobniej szukany przez nas ciag ma dlugosc >=13
    # zeby nie sprawdzac wszystkich ciagow od razu generujemy jedynie ciagi w ktorych cyfry sa nierosnace bo jest ich dla 13 jedynie 497 419
    # w porownaniu do wszystkich mozliwych ciagow ktorych jest az 13^10
    # Pozostaje tylko idac od najmniejszej liczby sprawdzic ktora z nich jest pierwsza i numer jest znaleziony
    for i in range(13, 20):
        print(f"Searching combinations of length {i}:")
        combs = search_combs(i)
        if combs is not None:
            print(f"Found smallest number fitting restrictions: {combs}")
            break
        else: print("Not found fitting given restrictions")

if __name__ == '__main__':
    main()