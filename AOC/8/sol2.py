import sys

sys.setrecursionlimit(2000)

def dist_sq(p1, p2):
    return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 + (p1[2] - p2[2])**2

coordinates = []
while True:
    try:
        raw = input()
        cords = [int(i) for i in raw.split(',')]
        coordinates.append(cords)
    except EOFError:
        break

N = len(coordinates)

edges = []
for i in range(N):
    for j in range(i + 1, N):
        d = dist_sq(coordinates[i], coordinates[j])
        edges.append((d, i, j))

edges.sort(key=lambda x: x[0])

parent = list(range(N))
num_groups = N

def find(i):
    if parent[i] != i:
        parent[i] = find(parent[i])
    return parent[i]

def union(i, j):
    global num_groups
    root_i = find(i)
    root_j = find(j)
    
    if root_i != root_j:
        parent[root_j] = root_i
        num_groups -= 1
        return True
    return False

result = 0

for d, p1, p2 in edges:
    if union(p1, p2):
        if num_groups == 1:
            result = coordinates[p1][0] * coordinates[p2][0]
            break

print(result)
