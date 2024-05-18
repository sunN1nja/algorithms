def dfs_recursive(graph, start, visited=None):
    """
    Рекурсивная функция для реализации поиска в глубину.

    :param graph: Граф, представленный в виде словаря смежности.
    :param start: Начальный узел.
    :param visited: Множество посещённых узлов.
    :return: None
    """
    if visited is None:
        visited = set()
    
    visited.add(start)
    print(start, end=' ')  # Выводим текущий узел

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)

# Пример использования
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

print("Рекурсивный DFS:")
dfs_recursive(graph, 'A')