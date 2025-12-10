def hanoi(n, a, b, c) -> None:
    if n == 0: return
    hanoi(n-1, a, c, b)
    print(f"{a} -> {c}")
    hanoi(n-1, b, a, c)

hanoi(4, 'A', 'B', 'C')
