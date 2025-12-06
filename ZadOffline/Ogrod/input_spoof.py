import sys

def main():
    raw = sys.stdin.read().split()

    if not raw:
        return

    data = iter(raw)

    N = int(next(data))
    L = int(next(data))


    #print(f"{N}.{L}", end="")
    dat = []
    for _ in range(L):
        w = int(next(data))
        k = int(next(data))
        angle = int(next(data))
        if angle == 45:
            angle = ')' 
        elif angle == 135:
            angle = '(' 
        else: angle = '|' 
        dat.append((w,k,angle))


    if len(dat) > 10:
        for i in range(10, len(dat)):
            w, k, angle = dat[i]
            print(f"{w},{k}{angle}",end='')

    print()


        
if __name__ == "__main__":
    main()
