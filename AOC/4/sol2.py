
def poss(n:int, m:int, r:int, k:int) -> bool:
    return (0 <= r < n and 0 <= k < m)

def bet_solve(grid: list[list[str]]) -> int:

    n = len(grid)
    m = len(grid[0])

    deltas = [(1,0), (-1,0), (1, 1), (1, -1), (-1, 1), (-1, -1), (0, 1), (0, -1)]
    taken = 0

    occ = [[0 for _ in range(m)] for _ in range(n)]
    seen = [[False for _ in range(m)] for _ in range(n)]
    queue:list[tuple[int,int]] = list()

    for r in range(n):
        for k in range(m):
            if grid[r][k] != '@': continue
            for delta in deltas:
                dr, dk = delta
                if poss(n, m, r+dr, k+dk):
                    if grid[r+dr][k+dk] == '@':
                        occ[r][k] += 1
            if occ[r][k] < 4:
                queue.append((r, k))
                seen[r][k] = True

    while len(queue) > 0:
        r, k = queue.pop() 

        occ[r][k]= 0
        taken += 1

        for delta in deltas:
            dr, dk = delta
            if poss(n, m, r+dr, k+dk):
                if occ[r+dr][k+dk] == 0: continue
                occ[r+dr][k+dk] -= 1
                if occ[r+dr][k+dk] < 4 and not seen[r+dr][k+dk]:
                    queue.append((r+dr, k+dk))
                    seen[r+dr][k+dk] = True


    return taken 

grid: list[list[str]] = []
while True:
    try:
        line = input()
        if not line: break
        grid.append(list(line))

    except EOFError:
        break
print(bet_solve(grid))


