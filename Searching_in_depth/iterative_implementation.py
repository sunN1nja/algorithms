def dfs_iterative(graph, start):
    """
    Итеративная функция для реализации поиска в глубину.

    :param graph: Граф, представленный в виде словаря смежности.
    :param start: Начальный узел.
    :return: None
    """
    visited = set()
    stack = [start]

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            print(vertex, end=' ')  # Выводим текущий узел
            stack.extend(neighbor for neighbor in graph[vertex] if neighbor not in visited)

# Пример использования
print("\nИтеративный DFS:")
dfs_iterative(graph, 'A')