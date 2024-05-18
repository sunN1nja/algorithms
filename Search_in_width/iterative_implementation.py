from collections import deque

def bfs(graph, start):
    """
    Итеративная функция для реализации поиска в ширину.

    :param graph: Граф, представленный в виде словаря смежности.
    :param start: Начальный узел.
    :return: None
    """
    visited = set()
    queue = deque([start])

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            print(vertex, end=' ')  # Выводим текущий узел

            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)

# Пример использования
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

print("Итеративный BFS:")
bfs(graph, 'A')