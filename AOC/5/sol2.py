
ranges = []
while True:
    raw = input()
    if raw == '': break

    p, k = raw.split('-')
    ranges.append((int(p), int(k)))

while True:
    try:
        _ = input()
    except EOFError:
        break


ranges = sorted(ranges)
merged = []

curr_start, curr_end = ranges[0]

for i in range(1, len(ranges)):
    next_start, next_end = ranges[i]

    if next_start <= curr_end:
        curr_end = max(curr_end, next_end)
    else:
        merged.append((curr_start, curr_end))
        curr_start, curr_end = next_start, next_end

merged.append((curr_start, curr_end))



sum = 0
for m in merged:
    sum += m[1] - m[0] + 1
print(sum)
    
