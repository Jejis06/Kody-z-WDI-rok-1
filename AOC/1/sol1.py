dial = 50
enc_of_O = 0

while True:
    try:
        rot = input()
        if not rot: continue

        dir = rot[0]
        amm = int(rot[1:])

        if dir == 'R': dial += amm
        else: dial -= amm

        dial = dial % 100

        if dial == 0: enc_of_O += 1

    except EOFError:
        break
print(enc_of_O)


