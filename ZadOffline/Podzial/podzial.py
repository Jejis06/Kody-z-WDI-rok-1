def unique_nums(s: str) -> bool:
    if len(s) > 10: return False
    return len(set(s)) == len(s)

def is_prime(num: int) -> bool:
    if num < 2: return False
    if num == 2: return True
    if num % 2 == 0: return False

    i = 3
    while i*i <= num:
        if num % i == 0:
            return False
        i += 2
    return True


import sys
digits = ''.join(i for i in sys.stdin.read().split())
N = len(digits)


maxDivide = 1000000

dp = [maxDivide for _ in range(N+1)]
dp[0] = 0

for i in range(1, N+1):

    maxlen = min(10, i)

    for back in range(1, maxlen + 1):
        block_beg = i - back


        if i == N and block_beg == 0:
            continue

        sub = digits[block_beg : i]
        num = int(sub)

        if not unique_nums(sub): continue
        if not is_prime(num): continue

        if dp[block_beg] != maxDivide:
            dp[i] = min(dp[i], dp[block_beg] + 1)

if dp[N] == maxDivide:
    print("BRAK")
else:
    print(dp[N])
