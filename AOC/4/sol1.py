
grid: list[list[str]] = []
while True:
    try:
        line = input()
        if not line: break
        grid.append(list(line))

    except EOFError:
        break

n = len(grid)
m = len(grid[0])
deltas = [(1,0), (-1,0), (1, 1), (1, -1), (-1, 1), (-1, -1), (0, 1), (0, -1)]

avail = 0

for r in range(n):
    for k in range(m):
        sum = 0
        if grid[r][k] != '@':
            continue
        for delta in deltas:
            dr, dk = delta
            if 0 <= r + dr < n and 0 <= k + dk < m:
                v = grid[r+dr][k+dk]
                sum += (v == '@')
        if sum < 4:
            avail += 1


print(avail)
