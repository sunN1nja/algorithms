import heapq

def dijkstra(graph, start):
    """
    Функция для реализации алгоритма Дейкстры.

    :param graph: Граф, представленный в виде словаря смежности с весами ребер.
    :param start: Начальный узел.
    :return: Словарь с минимальными расстояниями от начального узла до всех остальных узлов.
    """
    # Инициализация
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Если извлеченное расстояние больше текущего, пропускаем узел
        if current_distance > distances[current_vertex]:
            continue

        # Проверяем всех соседей текущего узла
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            # Если найден более короткий путь к соседу, обновляем расстояние
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Пример использования
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

start_node = 'A'
distances = dijkstra(graph, start_node)
print(f"Минимальные расстояния от узла {start_node}: {distances}")