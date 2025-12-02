dial = 50
enc_of_O = 0

while True:
    try:
        rot = input()
        dir = rot[0]
        amm = int(rot[1:])

        if dir == 'R': 
            target = dial + amm
            encs = (target // 100) - (dial // 100)
            enc_of_O += encs
            dial = target % 100
        else:
            start_pos = dial - 1
            end_pos = dial - amm - 1
            encs = (start_pos // 100) - (end_pos // 100)
            enc_of_O += encs
            dial = (dial - amm) % 100

    except EOFError:
        break
print(enc_of_O)


