def pal(a,b,s="") -> None:
    if a == b == 0:
        print(s)
        return 

    if a > 1: 
        pal(a-2, b, 'A' + s + 'A')
    if b > 1: 
        pal(a, b-2, 'B' + s + 'B')


def main(a, b):
    pal(a-1, b, 'A')
    pal(a, b-1, 'B')
    pal(a, b, '')

main(3,2)
