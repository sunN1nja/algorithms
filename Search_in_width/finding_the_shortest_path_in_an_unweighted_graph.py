def bfs_shortest_path(graph, start, goal):
    """
    Функция для поиска кратчайшего пути с использованием BFS.

    :param graph: Граф, представленный в виде словаря смежности.
    :param start: Начальный узел.
    :param goal: Целевой узел.
    :return: Список узлов, представляющий кратчайший путь.
    """
    queue = deque([(start, [start])])
    visited = set()

    while queue:
        (vertex, path) = queue.popleft()
        for next in graph[vertex]:
            if next not in visited:
                if next == goal:
                    return path + [next]
                else:
                    queue.append((next, path + [next]))
                visited.add(next)

# Пример использования
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

print("\nКратчайший путь BFS:", bfs_shortest_path(graph, 'A', 'F'))