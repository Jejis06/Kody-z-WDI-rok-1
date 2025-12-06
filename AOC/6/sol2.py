lines: list[str] = []
while True:
    try:
        raw = input()
        lines.append(raw)
    except EOFError:
        break

# 123 328  51 64 
#  45 64  387 23 
#   6 98  215 314
# *   +   *   + 

sep_line = len(lines) - 1
sepators = []

for i in range(1, len( lines[sep_line] )):
    if lines[sep_line][i] != " ":
        sepators.append(i-1)

nums = [0 for _ in range(len(lines[0]))]
for i in range(len(lines) - 1):
    line = list(lines[i])
    for j in range(len(line)):
        if line[j] == ' ' and j not in sepators:
            line[j] = '0'
        if line[j] != ' ':
            if int(line[j]) != 0:
                nums[j] = 10 * nums[j] + int(line[j])
    #print(line)
operators = [i for i in lines[sep_line].split(' ') if i != '']
curr_num = 0

tuples = []
t = []
for num in nums:
    if num != 0:
        t.append(num)
    else:
        tuples.append(t)
        t = []
tuples.append(t)


sum = 0
for t,op in zip(tuples, operators):
    r = 0
    if op == '*':
        r = 1
        for nu in t:
            r *= nu
    elif op == "+":
        for nu in t:
            r += nu
    sum += r
print(sum)
