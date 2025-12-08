#from math import sqrt



connections = []
def connect(p1: int, p2:int) -> None:
    global connections
    N = len(connections)
    if N == 0:
        connections.append([p1, p2])
        return

    group1 = -1
    group2 = -1

    for i in range(N):
        if p1 in connections[i]:
            group1 = i
            break

    for i in range(N):
        if p2 in connections[i]:
            group2 = i
            break

    if group1 == group2 and group1 != -1 and group2 != -1:
        return

    if group1 == -1 and group2 == -1:
        connections.append([p1, p2])
    elif group1 == -1 and group2 != -1:
        connections[group2].append(p1)
    elif group1 != -1 and group2 == -1:
        connections[group1].append(p2)
    elif group1 != -1 and group2 != -1:
        connections[group1].extend(connections[group2])
        del connections[group2]







# sqrt not needed since only comparison is needed
def dist(p1:list[int], p2:list[int]) -> int:
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2 + (p1[2] - p2[2]) ** 2)

coordinates:list[list[int]]= []
while True:
    try:
        raw = input()
        cords = [int(i) for i in raw.split(',')]
        coordinates.append(cords)
    except EOFError:
        break
#print(coordinates)


discovered_pairs = {}

for k in range(1000):
    min_dist = float('inf')
    mi = tuple() 
    for i in range(len(coordinates)-1):
        for j in range(i, len(coordinates)):
            if (i, j) not in discovered_pairs and (j, i) not in discovered_pairs and i != j and dist(coordinates[i], coordinates[j]) < min_dist:
                min_dist = dist(coordinates[i], coordinates[j])
                mi = (i, j)
    discovered_pairs[mi] = 1
    connect(mi[0], mi[1])

connections = sorted(connections, key=lambda x: len(x), reverse = True)
res = len(connections[0]) * len(connections[1]) * len(connections[2])
print(res)



