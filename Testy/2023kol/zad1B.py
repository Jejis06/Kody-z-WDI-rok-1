
def check_sudoku(arr: list[list[int]]) -> tuple[set[int], set[int]]:
    N = 9
    wrong_V = set()
    wrong_H = set()

    for wiersz in range(N):
        seen = 0
        for i in range(N):
            num = arr[wiersz][i]-1
            #print(num+1, end=' ')
            if (seen >> num) == 1:
                box = (i // 3) + 3 * (wiersz // 3)
                wrong_V.add(box + 1)
            seen |= 1 << num

    for kolumna in range(N):
        seen = 0
        for i in range(N):
            num = arr[i][kolumna] - 1
            if (seen >> num) == 1:
                box = (i//3) * 3 + (kolumna//3)
                wrong_H.add(box+1)
            seen |= 1 << num
    return (wrong_V, wrong_H) 

a = '''8 1 2 7 5 3 6 4 9
9 4 3 6 8 2 1 7 5
6 7 5 4 9 1 2 8 3
1 5 4 3 6 8 8 9 6
3 6 9 9 1 7 7 2 1
2 8 7 4 5 2 5 3 4
5 2 1 9 7 4 2 3 7
4 3 8 5 2 6 8 4 5
7 9 6 3 1 8 1 6 9'''
a = a.split('\n')
arr = []
for x in a:
    row = x.split(' ')
    arr.append([int(i) for i in row])

print(check_sudoku(arr))
