
def sklej(arr):
    # 8 cyfrowe liczby
    N = len(arr)

    conn = 0
    sumval = 0
    max_conn_val = 0

    for i in range(N-1):
        a = 0
        b = 0
        M1 = int(1e2)
        M = int(1e7)
        for j in range(3):
            a = (arr[i] // M1) % 10 + a * 10
            b = (arr[i+1] // M) % 10 + b * 10
            M //= 10
            M1 //=10
        if a == b:
            conn += 1
            sumval += a
            max_conn_val = max(max_conn_val, sumval)
        elif a - (a//100)*100 == b // 10:
            conn += 1
            sumval += b // 10
            max_conn_val = max(max_conn_val, sumval)
        else:
            sumval = 0

    if conn+1 == N:
        return -1
    return max_conn_val

#         210  210
#l = [12345678, 78854321]
#l = [12345678, 78854321, 77777777, 77777777,77777777]
#l = [77777777, 88888888, 99999999, 12333123]
l =  [77777777 for _ in range(1_000_000)]; l.append(88888888)
print(sklej(l))

