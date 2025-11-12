import sys
instr = sys.stdin.readline

occurances = {}

arrid = 0

def mancher(line_raw: str) -> None:
    n = len(line_raw)
    line = '*' + line_raw + '%'

    for parity in range(2):
        current_radius = 0
        center = 1
        while center <= n:
            while line[center - current_radius - 1] == line[center + parity + current_radius]:
                current_radius += 1
            evenOdd[arrid][parity][center] = current_radius

            skip = 1
            while (
                    skip < current_radius and 
                    evenOdd[arrid][parity][center-skip] != current_radius - skip
            ):
                evenOdd[arrid][parity][center + skip] = min(
                        evenOdd[arrid][parity][center - skip],
                        current_radius - skip
                )
                skip += 1

            current_radius = max(current_radius - skip, 0)
            center += skip



# input
N = int(instr().strip())

# odd0[0] == evenOdd[0][1][0]
# even0[0] == evenOdd[0][0][0]

evenOdd = [[[0 for _ in range(N+1)] for _ in range(2)] for _ in range(6 * N - 18)] 
grid = [instr().strip() for _ in range(N)]

lines_data: list[str] = []

# data processing
for r in range(N):
    lines_data.append(grid[r])

for c in range(N):
    lines_data.append("".join(grid[r][c] for r in range(N)))

for k in range(5-N, N-4):
    line: list[str] = []
    for c in range(max(0, -k), min(N, N - k)):
        r = k + c
        line.append(grid[r][c])
    lines_data.append("".join(line))

for k in range(4, 2 * N - 5):
    line = []
    for c in range(max(0, k - N + 1), min(N, k + 1)):
        r = k - c
        line.append(grid[r][c])
    lines_data.append("".join(line))


# solution 
for line in lines_data:
    n = len(line)
    mancher(line)
    #print(f'-----------------{line}-{n}-----------------')

    for parity in range(2):
        for i in range(1, n+1):
            l = 2 * evenOdd[arrid][parity][i] + parity 
            if l < 5 : continue

            pal = line[ i - 1 - evenOdd[arrid][parity][i]  :  i - 1 + evenOdd[arrid][parity][i] + parity]
            #print(pal, parity)

            if pal in occurances: occurances[pal] += 1
            else: occurances[pal] = 1

            if occurances[pal] == 2:
                print(pal)
                break
    arrid += 1

