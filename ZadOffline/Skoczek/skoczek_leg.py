from sys import stdin
from heapq import heappop as pq_pop
from heapq import heappush as pq_push

min_path = float('inf')

def solve(cups:list[int], energy:int=0, pos:int=0, path:int=0) -> None:
    global min_path
    n = len(cups)
    if n-1 == pos:
        min_path = min(path, min_path)
        return
    if path > min_path: return

    energy += cups[pos]
    for j in range(pos+1, n):
        cost = j - pos
        if 0 <= cost <= energy:
            solve(cups, energy - cost, j, path+1)

def dijkstra_solve(cups:list[int]) -> int | str:
    min_cost = float('inf')
    N = len(cups)

    vis = [-1 for _ in range(N)]
    q:list[tuple[int,int,int]] = []

    pq_push(q, (0, 0, 0))
    while len(q) > 0:
        curr_cost, curr_pos, curr_energy = pq_pop(q)
        curr_energy += cups[curr_pos]
        
        if curr_pos == N-1:
            min_cost = min(curr_cost, min_cost)
            break

        if vis[curr_pos] >= curr_energy:
            continue
        vis[curr_pos] = curr_energy

        max_range = min(N, curr_pos + 1 + curr_energy)

        for pos in range(curr_pos+1, max_range):
            energy_diff = pos - curr_pos
            pq_push(q ,(curr_cost+1, pos, curr_energy - energy_diff))

    return int(min_cost) if min_cost != float('inf') else 'BRAK'


def main():
    global min_path
    inp = iter( stdin.read().split() )
    n:int = int(next(inp))

    arr = [0 for _ in range(n)]
    for i in range(n):
        arr[i] = int(next(inp))
    print(n, arr)
    #solve(arr)

    min_path = min_path if min_path != float('inf') else 'BRAK'
    print('slow')
    print(min_path)
    print('dijkstra')
    print(dijkstra_solve(arr))

    pass
    

if __name__ == '__main__':
    main()
