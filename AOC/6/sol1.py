lines = []
while True:
    try:
        raw = input()
        line = [i for i in raw.split(' ') if i != '']
        lines.append(line)
    except EOFError:
        break
N = len(lines[0])

eqations = [[] for _ in range(N)]
operatots = iter(lines[len(lines)-1])
for i in range(len(lines) - 1):
    for el in range(len(lines[i])):
        eqations[el].append(int(lines[i][el]))

sum = 0
for eq in eqations:
    op = next(operatots)
    if op == '*':
        res = 1
        for num in eq:
            res *= num
    elif op == '+':
        res = 0
        for num in eq:
            res += num
    sum += res
print(sum)


