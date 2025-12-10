from itertools import product 

def get_solution_to_matrix(matrix:list[list[int]], pivots:list[tuple[int,int]],
                           free_values:tuple[int,...], free_cols:list[int], M:int) -> list[int]:
    res = [0] * M
    for i, val in enumerate(free_values):
        col_ind = free_cols[i]
        res[col_ind] = val

    for row_ind, col_ind in reversed(pivots):
        val = matrix[row_ind][-1]
        for c in range(col_ind + 1, M):
            if matrix[row_ind][c] == 1:
                val ^= res[c]

        res[col_ind] = val
    return res


def process(line: str) -> int:
    diagram = line.split(']')[0][1:]
    target = [1 if i == '#' else 0 for i in diagram]
    buttons_raw = line.split(' ')[1:][:-1]

    N = len(target)
    M = len(buttons_raw)

    button_maps:list[list[int]] = []
    for raw_button in buttons_raw:
        button_map = [0] * N
        for i in raw_button[1:][:-1].split(','):
            button_map[int(i)] = 1
        button_maps.append(button_map)

    matrix:list[list[int]] = []
    for r in range(N):
        row:list[int] = [button[r] for button in button_maps]
        row.append(target[r])
        matrix.append(row)

    pivot_row = 0
    pivots:list[tuple[int, int]] = []

    # Metoda Gausasa
    for col in range(M):
        if pivot_row >= N:
            break
        swap_row = -1
        for r in range(pivot_row, N):
            if matrix[r][col] == 1:
                swap_row = r
                break

        if swap_row == -1:
            continue
        matrix[pivot_row], matrix[swap_row] = matrix[swap_row], matrix[pivot_row]

        for r in range(N):
            if r != pivot_row and matrix[r][col] == 1:
                for c in range(len(matrix[r])):
                    matrix[r][c] ^= matrix[pivot_row][c]

        pivots.append((pivot_row, col))
        pivot_row += 1


    pivot_cols = set(c for _,c in pivots)
    free_cols = [c for c in range(M) if c not in pivot_cols]

    min_presses = float('inf')
    for free_vals in product([0, 1], repeat=len(free_cols)):
        sol = get_solution_to_matrix(matrix, pivots, free_vals, free_cols, M)
        presses = sum(sol)
        if presses < min_presses:
            min_presses = presses

    return int(min_presses) 


s = 0
# MACIERZE >:(((
while True:
    try:
        raw = input()
        s += process(raw)
    except EOFError:
        break
print(s)

