class Edge:
    def __init__(self, u, v, weight):
        self.u = u
        self.v = v
        self.weight = weight

def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])

def union(parent, rank, x, y):
    root_x = find(parent, x)
    root_y = find(parent, y)
    if rank[root_x] < rank[root_y]:
        parent[root_x] = root_y
    elif rank[root_x] > rank[root_y]:
        parent[root_y] = root_x
    else:
        parent[root_y] = root_x
        rank[root_x] += 1

def kruskal(graph, vertices):
    result = []
    graph.sort(key=lambda x: x.weight)
    parent = []
    rank = []
    for node in range(vertices):
        parent.append(node)
        rank.append(0)
    e = 0
    i = 0
    while e < vertices - 1:
        u, v, weight = graph[i].u, graph[i].v, graph[i].weight
        i += 1
        x = find(parent, u)
        y = find(parent, v)
        if x != y:
            e += 1
            result.append((u, v, weight))
            union(parent, rank, x, y)
    return result

# Пример использования
edges = [
    Edge(0, 1, 10),
    Edge(0, 2, 6),
    Edge(0, 3, 5),
    Edge(1, 3, 15),
    Edge(2, 3, 4)
]
vertices = 4
mst = kruskal(edges, vertices)
print("Минимальное остовное дерево:")
for u, v, weight in mst:
    print(f"Ребро {u}-{v} с весом {weight}")
# Вывод:
# Минимальное остовное дерево:
# Ребро 2-3 с весом 4
# Ребро 0-3 с весом 5
# Ребро 0-1 с весом 10