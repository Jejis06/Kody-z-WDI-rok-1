
def find_max_sum(s: str, needed: int = 12) -> int:
    n = len(s)
    if n < needed:
        return 0

    curr_ind = 0
    res = 0

    for i in range(needed):
        res *= 10
        remaining = needed - i - 1
        window_end = n - remaining

        best_num = -1
        best_num_ind = window_end

        for j in range(window_end - 1, curr_ind - 1, -1):
            curr_num = int(s[j])
            if curr_num >= best_num:
                best_num = curr_num
                best_num_ind = j

        best_num_ind -= curr_ind

        res = (res + best_num)
        curr_ind += best_num_ind + 1

    return res





max_sum = 0
while True:
    try:
        raw = input()
        if not raw: break

        max_sum += find_max_sum(raw)

    except EOFError:
        break
print(max_sum)
