arr:list[str]= []

while True:
    try:
        raw = input()
        arr.append(raw)
    except EOFError:
        break
sw, sk = 0, arr[0].find('S')
beams = [sk]
N = len(arr[0])

res = 0
for line_ind in range(1, len(arr)):
    line = arr[line_ind]
    new_beams = []
    # print(beams)
    for beam in beams:
        if line[beam] == '^':
            res += 1
            if N > beam + 1 >= 0:
                new_beams.append(beam + 1)
            if N > beam - 1 >= 0:
                new_beams.append(beam - 1)
        else:
            new_beams.append(beam)
    beams = list(set(new_beams))

print(res)

