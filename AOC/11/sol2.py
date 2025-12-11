from functools import lru_cache
# grafowka
graph:dict[str, list[str]] = {}

res = 0

# dac/ fft
@lru_cache(maxsize=None)
def dfs(node:str = "svr", dac:bool=False, fft:bool=False) -> int:
    if node == 'out':
        return 1 if dac and fft else 0

    if node not in graph:
        return 0

    paths = 0
    for child in graph[node]:
        dac_1 = dac or (child == 'dac')
        fft_1 = fft or (child == 'fft')

        paths += dfs(child, dac_1, fft_1)
    return paths

while True:
    try:
        raw = input()
        conn = raw.split(':')

        parent = conn[0]
        verts = conn[1].split(' ')[1:]

        if parent not in graph: graph[parent] = []
        for vert in verts:
            graph[parent].append(vert)

    except EOFError:
        break
print(dfs())
