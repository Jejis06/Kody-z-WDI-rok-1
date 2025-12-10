import sys
from collections import deque

pairs = []
while True:
    try:
        raw = input()
        if not raw: break
        raw = [int(i) for i in raw.split(',')]
        pairs.append(raw)
    except EOFError:
        break

xs = sorted(list(set(p[0] for p in pairs)))
ys = sorted(list(set(p[1] for p in pairs)))

xi = {x: i + 1 for i, x in enumerate(xs)}
yi = {y: i + 1 for i, y in enumerate(ys)}

w = len(xs) + 2
h = len(ys) + 2

grid = [[0] * w for _ in range(h)]

for i in range(len(pairs)):
    p1 = pairs[i]
    p2 = pairs[(i + 1) % len(pairs)]
    
    c1x, c1y = xi[p1[0]], yi[p1[1]]
    c2x, c2y = xi[p2[0]], yi[p2[1]]
    
    if c1x == c2x:
        for y in range(min(c1y, c2y), max(c1y, c2y) + 1):
            grid[y][c1x] = 1
    else:
        for x in range(min(c1x, c2x), max(c1x, c2x) + 1):
            grid[c1y][x] = 1

q = deque([(0, 0)])
seen = set([(0, 0)])
grid[0][0] = 2

while q:
    cx, cy = q.popleft()
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nx, ny = cx + dx, cy + dy
        if 0 <= nx < w and 0 <= ny < h:
            if grid[ny][nx] == 0:
                grid[ny][nx] = 2
                q.append((nx, ny))

pref = [[0] * (w + 1) for _ in range(h + 1)]
for y in range(h):
    for x in range(w):
        val = 1 if grid[y][x] != 2 else 0
        pref[y+1][x+1] = val + pref[y][x+1] + pref[y+1][x] - pref[y][x]

max_area = 0

for i in range(len(pairs)):
    for j in range(i + 1, len(pairs)):
        p1 = pairs[i]
        p2 = pairs[j]
        
        x1, y1 = xi[p1[0]], yi[p1[1]]
        x2, y2 = xi[p2[0]], yi[p2[1]]

        min_x, max_x = min(x1, x2), max(x1, x2)
        min_y, max_y = min(y1, y2), max(y1, y2)

        expected = (max_x - min_x + 1) * (max_y - min_y + 1)
        actual = pref[max_y+1][max_x+1] - pref[min_y][max_x+1] - pref[max_y+1][min_x] + pref[min_y][min_x]

        if expected == actual:
            area = (abs(p1[0] - p2[0]) + 1) * (abs(p1[1] - p2[1]) + 1)
            if area > max_area:
                max_area = area

print(max_area)
