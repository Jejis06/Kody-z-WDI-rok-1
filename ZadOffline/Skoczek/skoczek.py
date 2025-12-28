from sys import stdin
from collections import deque


def bfs_solve(cups:list[int]) -> int | str:
    N = len(cups)

    vis = [-1 for _ in range(N)]
    q = deque([(0,0,0)])

    while q:
        curr_cost, curr_pos, curr_energy = q.popleft()
        curr_energy += cups[curr_pos]
        
        if curr_pos == N-1:
            return curr_cost

        if vis[curr_pos] >= curr_energy:
            continue
        vis[curr_pos] = curr_energy

        max_range = min(N, curr_pos + 1 + curr_energy)

        for pos in range(curr_pos+1, max_range):
            energy_diff = pos - curr_pos
            q.append((curr_cost+1, pos, curr_energy - energy_diff))

    return 'BRAK'


def main():
    global min_path
    inp = iter( stdin.read().split() )
    n:int = int(next(inp))

    arr = [0 for _ in range(n)]
    for i in range(n):
        arr[i] = int(next(inp))

    print(bfs_solve(arr))
    pass

if __name__ == '__main__':
    main()
