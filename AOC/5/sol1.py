ranges = []
while True:
    raw = input()
    if raw == '': break

    p, k = raw.split('-')
    ranges.append((int(p), int(k)))


valid = 0
while True:
    try:
        raw = input()
        num = int(raw)
        for r in ranges:
            if r[0] <= num <= r[1]:
                valid += 1
                break

    except EOFError:
        break
print(valid)
