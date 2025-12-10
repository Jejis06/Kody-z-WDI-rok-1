from math import gcd
from heapq import heappush as pq_push
from heapq import heappop as pq_pop
import time

min_amm = float('inf')
def recursive_solve(caps:list[int], state:tuple[int,...], step:int, amm:int) -> None:
    global min_amm


    if amm >= min_amm:
        return

    if 1 in state:
        min_amm = amm
        return

    if step >= 8:
        return

    N = len(caps)
    for src in range(N):
        if state[src] == 0:
            continue
        for dst in range(N):
            if src == dst: continue

            space = caps[dst] - state[dst]
            if space > 0:
                t_amm = min(space, state[src])

                new_state = list(state)
                new_state[src] -= t_amm
                new_state[dst] += t_amm
                new_state = tuple(new_state)

                recursive_solve(caps, new_state, step+1, amm + t_amm)

def fast_sol(caps:list[int]) -> int:
    N = len(caps)
    initial_state = [0] * N
    initial_state[0] = caps[0]

    initial_state = tuple(initial_state)

    pq = [(0, 0, initial_state)]
    vis: set[tuple[tuple[int,...], int]] = set()

    while len(pq) > 0:
        cost, step, state = pq_pop(pq)

        if 1 in state: return cost
        if step >= 8: continue

        state_key = (state, step)
        if state_key in vis: continue
        vis.add(state_key)

        for src in range(N):
            if state[src] <= 0: continue
            for dst in range(N):
                if src == dst: continue
                space = caps[dst] - state[dst]

                if space > 0:
                    curr_cost = min(space, state[src])
                    if curr_cost > 0: 
                        new_state = list(state)
                        new_state[src] -= curr_cost
                        new_state[dst] += curr_cost
                        new_state = tuple(new_state)

                        if (new_state, cost+curr_cost) not in vis:
                            pq_push(pq, (cost+curr_cost, step+1, new_state))
    return -1



def main() -> None:
    global min_amm
    N = int(input())
    sizes = [int(i) for i in input().split(' ')]

    state = [0] * N
    state[0] = sizes[0]

    # Rozwiazanie rekurencyjne DFS
    recursive_solve(sizes, tuple(state), 0, 0)
    min_amm = min_amm if min_amm != float('inf') else 'BRAK'
    print(min_amm)

    # Rozwiazanie prawie liniowe DAjkstra
    res = fast_sol(sizes)
    res = res if res != -1 else 'BRAK'
    print(res)



    return

if __name__ == "__main__":
    main()

