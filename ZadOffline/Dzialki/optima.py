from sys import stdin

inp = iter( stdin.read().split() )

n = int(next(inp))
plots = [0] * n

for i in range(n): plots[i] = int(next(inp))

plots[1] = max(plots[0], plots[1])
for i in range(2, n): plots[i] = max(plots[i-1], plots[i-2] + plots[i])

print(plots[n-1])
