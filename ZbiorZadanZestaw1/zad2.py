# 3 * (100 * a + 10 * b + c) = 100b + 10b + b
# 300a + 30b + 3c = 100b + 10b + b
# 300a + 3c = 100b + b - 20b
# 300a + 3c = (100 + 1 - 20)b
# 300a + 3c = 81b



for a in range(0,10):
    for b in range(0,10):
        for c in range(0,10):
            if 300*a + 3*c == 81 * b:
                print(f"{a}{b}{c} + {a}{b}{c} + {a}{b}{c} = {b}{b}{b} | a: {a}, b: {b}, c: {c}")
