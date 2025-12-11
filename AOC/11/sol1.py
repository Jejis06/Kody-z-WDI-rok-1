
# grafowka
graph:dict[str, list[str]] = {}

res = 0

def dfs(node: str = "you"):
    global res
    for vert in graph[node]:
        if vert == 'out': 
            res += 1
            continue
        if vert == node: continue
        dfs(vert)

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
dfs()
print(res)
