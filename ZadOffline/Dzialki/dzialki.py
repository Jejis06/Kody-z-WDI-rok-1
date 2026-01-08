from sys import stdin
from math import ceil



# N: 3 <= N <= 100
def main() -> None:
    inp = iter( stdin.read().split() )

    n = int(next(inp))
    plots = [0] * n
    maxCosts = [0] * n # depek

    for i in range(n):
        plots[i] = int(next(inp))

    maxCosts[0] = plots[0]
    maxCosts[1] = max(plots[0], plots[1])

    for i in range(2, n):
        maxCosts[i] = max(maxCosts[i-1], maxCosts[i-2] + plots[i])
    print(maxCosts[n-1])


    pass

if __name__ == '__main__':
    main()
