from math import gcd
from heapq import heappush as pq_push
from heapq import heappop as pq_pop
import time
from gen import get_test


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

def run_test():
    global min_amm

    test = get_test()

    N = test['N']
    sizes = test['arr']

    # naj = sizes[0]
    # for s in sizes: naj = gcd(naj, s)
    #
    # if naj != 1: # test validity check
    #     print(f"najwDziel: {naj}")
    #     return

    state = [0] * N
    state[0] = sizes[0]

    t1 = time.time()
    recursive_solve(sizes, tuple(state), 0, 0)
    t2 = time.time()

    if min_amm == float('inf'): min_amm = -1
    print(f"rec_solve {min_amm} , {t2-t1}s")
    d1 = t2 - t1

    t1 = time.time()
    res = fast_sol(sizes)
    t2 = time.time()
    print(f"dijkstra_solve {res} , {t2-t1}s")
    d2 = t2 - t1
    print(f"STATS | N: {N}, DIFF: {d1-d2}, {(d1/d2):.2f}x speedup ")

    ok = min_amm == res
    min_amm = float('inf')


    return (N, d1-d2, (d1/d2), ok)


def main() -> None:
    num_tests = int(input("NUM TESTS: "))

    mean_diff = 0
    mean_N = 0
    mean_speedup = 0

    for _ in range(num_tests):
        n, diff, speedup, ok = run_test()
        if not ok:
            print("zle")
            break
        mean_diff += diff
        mean_N += n
        mean_speedup += speedup

    mean_diff /= num_tests
    mean_N /= num_tests
    mean_speedup /= num_tests

    print(F"STATS | mean_diff: {mean_diff:.4f}, mean_N: {mean_N:.4f}, mean_speedup: {mean_speedup:.4f}x")






    return

if __name__ == "__main__":
    main()

