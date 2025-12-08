
class FindOnion:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n  

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            if self.size[root_i] < self.size[root_j]:
                root_i, root_j = root_j, root_i
            self.parent[root_j] = root_i
            self.size[root_i] += self.size[root_j]
            return True
        return False

# sqrt not needed since only comparison is needed
def dist(p1:list[int], p2:list[int]) -> int:
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2 + (p1[2] - p2[2]) ** 2)

coordinates = []

while True:
    try:
        raw = input()
        cords = [int(i) for i in raw.split(',')]
        coordinates.append(cords)
    except EOFError:
        break

N = len(coordinates)

pairs = []
for i in range(N):
    for j in range(i + 1, N):
        d = dist(coordinates[i], coordinates[j])
        pairs.append((d, i, j))
pairs.sort(key=lambda x: x[0])

uni = FindOnion(N)
lim = 1000

for k in range(lim):
    _, p1, p2 = pairs[k]
    uni.union(p1, p2)

circuit_sizes = {}
for i in range(N):
    r = uni.find(i)
    circuit_sizes[r] = uni.size[r]
circuit_sizes = sorted(circuit_sizes.values(), reverse=True)
res = circuit_sizes[0] * circuit_sizes[1] * circuit_sizes[2]
print(res)


