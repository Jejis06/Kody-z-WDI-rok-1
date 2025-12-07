from _collections import defaultdict

arr:list[str]= []

while True:
    try:
        raw = input()
        arr.append(raw)
    except EOFError:
        break
sw, sk = 0, arr[0].find('S')
beams = defaultdict(int)
beams[sk] = 1
N = len(arr[0])

for line_ind in range(1, len(arr)):
    line = arr[line_ind]
    new_beams = defaultdict(int) 
    for beam, amm in beams.items():
        if line[beam] == '^':
            if N > beam + 1 >= 0:
                new_beams[beam + 1] += amm
            if N > beam - 1 >= 0:
                new_beams[beam - 1] += amm
        else:
            new_beams[beam] += amm
    beams = new_beams

print(sum(beams.values()))

