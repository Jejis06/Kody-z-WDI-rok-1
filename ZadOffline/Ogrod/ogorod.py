import sys

dirs = [(-1,0) ,(1,0), (0,-1), (0,1)]
# indeksy specjalne 'dirs'
# G=0
# D=1
# L=2
# P=3


dict_tii = dict[tuple[int, int],  int]
dict_tiit = dict[tuple[int, int],  tuple[int, int]]
set_ti = set[tuple[int, int]] 


def odbicie(dir_ind:int, angle:int) -> int:
    if angle == 45:
        return [3, 2, 1, 0][dir_ind]
    elif angle == 135:
        return [2, 3, 0, 1][dir_ind]
    return -1

def sciezka(start_w:int,
            start_k:int,
            start_d:int,
            mirrors:dict_tii,
            N:int
        ) -> tuple[set_ti, dict_tiit]:

    enc_mirrors:set_ti = set()
    visited:dict_tiit = {} # (w, k) -> dir_ind

    w, k = start_w, start_k
    dir_ind = start_d

    cntr = 0
    max_cntr = 4*N*N +110
    while 0 <= w < N and 0 <= k < N and cntr < max_cntr :
        cntr += 1 
        if (w, k) in mirrors:
            enc_mirrors.add((w, k))
            angle = mirrors[(w, k)]
            dir_ind = odbicie(dir_ind, angle)
        else:
            visited[(w, k)] = (dir_ind, cntr)

        dw, dk = dirs[dir_ind]
        w += dw
        k += dk
    return (enc_mirrors, visited)

def main():
    raw = sys.stdin.read().split()

    if not raw:
        return

    data = iter(raw)

    N = int(next(data))
    L = int(next(data))


    mirrors:dict_tii = {}
    for _ in range(L):
        w = int(next(data))
        k = int(next(data))
        angle = int(next(data))

        mirrors[(w, k)] = angle

    # Szukanie Zmienionego lustra
    start_mirrors_hit, path_start = sciezka(0, 0, 1, mirrors, N)
    end_mirrors_hit, path_end = sciezka(N-1, N-1, 0, mirrors, N)

    bad_mirror = None 

    for mirror in mirrors:
        if mirror not in start_mirrors_hit and mirror not in end_mirrors_hit:
            bad_mirror = mirror
            break

    if bad_mirror is not None:
        print(f"{bad_mirror[0]} {bad_mirror[1]}")
    else:
        end_mirrors_hit = sorted(end_mirrors_hit)[1]
        print(f"{end_mirrors_hit[0]} {end_mirrors_hit[1]}")




    intersections = sorted(list(path_start.keys() & path_end.keys()), key=lambda x: path_start[x][1], reverse=True)

    opposite_direction = [1,0,3,2]
    for inter in intersections:
        curr_w, curr_k = inter 
        dir_start = path_start[inter][0]
        dir_needed = opposite_direction[path_end[inter][0]]

        if odbicie(dir_start, 45) == dir_needed or odbicie(dir_start, 135) == dir_needed:
            print(f"{curr_w} {curr_k}")
            return

    print(f"{intersections[0][0]} {intersections[0][1]}")

if __name__ == "__main__":
    main()
