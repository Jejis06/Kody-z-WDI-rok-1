
from math import gcd
from fractions import Fraction

def NWW(a, b) -> int:
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // gcd(a, b)

def frac_gcd(f1: Fraction, f2: Fraction) -> Fraction:
    num_gcd = gcd(f1.numerator, f2.numerator)
    den_nww = NWW(f1.denominator, f2.denominator)
    return Fraction(num_gcd, den_nww)

input_fractions = []

N = int(input().strip())
for i in range(N):
    lineRaw = input()
    a, b = lineRaw.split(' ')
    input_fractions.append( Fraction(int(a), int(b)) )

diffs = []
for i in range(N-1):
    diff = input_fractions[i+1] - input_fractions[i]
    diffs.append(diff)

r = diffs[0]
for i in range(1, len(diffs)):
    r = frac_gcd(r, diffs[i])

for i in range(N-1):
    s = input_fractions[i]
    e = input_fractions[i+1]

    gap = e - s
    missed = gap / r
    steps = int(missed)
    curr = s
    for _ in range(1, steps):
        curr += r
        print(f"{curr.numerator} {curr.denominator}")




