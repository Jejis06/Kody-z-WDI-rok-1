
pairs:list[list[int]] = []
while True:
    try:
        raw = input()
        # k, w
        raw = [int(i) for i in raw.split(',')]
        pairs.append(raw)
    except EOFError:
        break
pairs = sorted(pairs, key=lambda x : x[0])


max_area = 0
for i in range(len(pairs) - 1):
    p1 = pairs[i]
    for j in range(i+1, len(pairs)):
        p2 = pairs[j]
        if p2[1] > p1[1]: area = (p2[1] - p1[1] + 1) * (p2[0] - p1[0] + 1)
        else: area = (p1[1] - p2[1] + 1) * (p2[0] - p1[0] + 1)
        max_area = max(area, max_area)

print(max_area)


