max_sum = 0
while True:
    try:
        raw = input()
        if not raw: break

        curr_max = 0
        n = len(raw)
        for i in range(n):
            for j in range(i+1,n):
                curr_num = int(raw[i] + raw[j])
                curr_max = max(curr_num, curr_max)

        max_sum += curr_max

    except EOFError:
        break
print(max_sum)
