from fractions import Fraction

def search_min_presses(idx, free_cols, current_free_vals, pivots, aug_matrix, bounds, current_min):
    if sum(current_free_vals) >= current_min:
        return current_min

    if idx == len(free_cols):
        solution = [Fraction(0)] * len(aug_matrix[0])
        
        for i, f_col in enumerate(free_cols):
            solution[f_col] = Fraction(current_free_vals[i])

        current_sum = sum(current_free_vals)
        possible = True

        for p_col, p_row in pivots:
            val = aug_matrix[p_row][-1]
            for f_col in free_cols:
                if aug_matrix[p_row][f_col] != 0:
                    val -= aug_matrix[p_row][f_col] * solution[f_col]
            
            if val.denominator != 1 or val < 0:
                possible = False
                break
            
            current_sum += int(val)
        
        if possible:
            return min(current_min, current_sum)
        return current_min

    col_idx = free_cols[idx]
    limit = bounds[col_idx]
    
    local_min = current_min
    
    for val in range(limit + 1):
        current_free_vals.append(val)
        local_min = search_min_presses(idx + 1, free_cols, current_free_vals, pivots, aug_matrix, bounds, local_min)
        current_free_vals.pop()
        
    return local_min

def process(line: str) -> int:
    start_idx = line.find('{')
    end_idx = line.find('}')
    if start_idx == -1 or end_idx == -1:
        return 0
        
    target_str = line[start_idx+1:end_idx]
    targets = [int(x) for x in target_str.split(',')]
    
    parts = line.split()
    buttons_raw = []
    for p in parts:
        if p.startswith('(') and p.endswith(')'):
            buttons_raw.append(p)

    N = len(targets)
    M = len(buttons_raw)

    matrix = []
    bounds = {}

    for col in range(M):
        bounds[col] = float('inf')

    for r in range(N):
        row = []
        for c, b_str in enumerate(buttons_raw):
            content = b_str[1:-1]
            indices = [int(x) for x in content.split(',')] if content else []
            
            val = 1 if r in indices else 0
            row.append(Fraction(val))
            
            if val == 1:
                bounds[c] = min(bounds[c], targets[r])
                
        row.append(Fraction(targets[r]))
        matrix.append(row)

    for c in range(M):
        if bounds[c] == float('inf'):
            bounds[c] = 0

    pivot_row = 0
    pivots = [] 
    
    for col in range(M):
        if pivot_row >= N:
            break
            
        swap_row = -1
        for r in range(pivot_row, N):
            if matrix[r][col] != 0:
                swap_row = r
                break
        
        if swap_row == -1:
            continue
            
        matrix[pivot_row], matrix[swap_row] = matrix[swap_row], matrix[pivot_row]
        
        scale = matrix[pivot_row][col]
        for c in range(col, M + 1):
            matrix[pivot_row][c] /= scale
            
        for r in range(N):
            if r != pivot_row and matrix[r][col] != 0:
                factor = matrix[r][col]
                for c in range(col, M + 1):
                    matrix[r][c] -= factor * matrix[pivot_row][c]
                    
        pivots.append((col, pivot_row))
        pivot_row += 1


    pivot_cols = set(c for c, _ in pivots)
    free_cols = [c for c in range(M) if c not in pivot_cols]
    
    free_cols.sort(key=lambda c: bounds[c])

    min_presses = search_min_presses(0, free_cols, [], pivots, matrix, bounds, float('inf'))

    return int(min_presses)

s = 0
while True:
    try:
        raw = input()
        s += process(raw)
    except EOFError:
        break
print(s)
