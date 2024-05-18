def floyd_warshall(graph):
    """
    Реализация алгоритма Флойда-Уоршелла для нахождения кратчайших путей между всеми парами вершин.

    :param graph: Граф, представленный в виде матрицы смежности, где graph[i][j] - вес ребра между вершинами i и j.
    :return: Матрица кратчайших расстояний между всеми парами вершин.
    """
    # Количество вершин в графе
    num_vertices = len(graph)
    
    # Инициализация матрицы расстояний
    dist = [[float('inf')] * num_vertices for _ in range(num_vertices)]
    
    for i in range(num_vertices):
        for j in range(num_vertices):
            if i == j:
                dist[i][j] = 0
            elif graph[i][j] != 0:
                dist[i][j] = graph[i][j]
    
    # Основной цикл алгоритма Флойда-Уоршелла
    for k in range(num_vertices):
        for i in range(num_vertices):
            for j in range(num_vertices):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    
    return dist

# Пример использования
graph = [
    [0, 3, float('inf'), 5],
    [2, 0, float('inf'), 4],
    [float('inf'), 1, 0, float('inf')],
    [float('inf'), float('inf'), 2, 0]
]

distances = floyd_warshall(graph)
print("Матрица кратчайших расстояний между всеми парами вершин:")
for row in distances:
    print(row)