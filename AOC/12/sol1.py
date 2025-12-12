import sys

raw = sys.stdin.read().split()
i = 0
masks:list[list[list[int]]] = []
requirements = []

while i < len(raw):
    if 'x' not in raw[i]:
        ind = int(raw[i][:-1])
        mask:list[list[int]] = []
        for j in range(i+1, i+4):
            mask.append([1 if k == '#' else 0 for k in raw[j]])
        masks.append(mask)
        i += 4
    else: break

N = len(masks)
requirements:list[tuple[tuple[int,int], list[int]]] = [] # static type hell

while i < len(raw):
    if 'x' in raw[i]:
        required:list[int] = []
        for j in range(i+1, i+N+1):
            required.append( int(raw[j]) )

        tup = raw[i].replace(':','').split('x')
        width = int( tup[0] )
        height = int( tup[1] )

        requirements.append(((width, height), required))
        i += N + 1
    else: i += 1


# Rozwiazanie
mask_areas:list[int] = []
for mask in masks:
    area = sum(sum(row) for row in mask)
    mask_areas.append(area)

valid = 0
for dims, counts in requirements:
    width, height = dims
    total_area = width * height

    total_presents_area = 0
    for ind, count in enumerate(counts):
        total_presents_area += count * mask_areas[ind]

    if total_presents_area <= total_area:
        valid += 1
print(valid)
