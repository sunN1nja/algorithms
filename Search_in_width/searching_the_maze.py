def bfs_maze(maze, start, end):
    """
    Функция для поиска пути в лабиринте с использованием BFS.

    :param maze: Двумерный массив, представляющий лабиринт.
    :param start: Начальная позиция (x, y).
    :param end: Конечная позиция (x, y).
    :return: Список позиций, представляющий путь.
    """
    queue = deque([(start, [start])])
    visited = set()
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Вправо, вниз, влево, вверх

    while queue:
        (current, path) = queue.popleft()
        if current == end:
            return path

        for direction in directions:
            next_position = (current[0] + direction[0], current[1] + direction[1])
            if (0 <= next_position[0] < len(maze) and
                0 <= next_position[1] < len(maze[0]) and
                maze[next_position[0]][next_position[1]] == 0 and
                next_position not in visited):
                queue.append((next_position, path + [next_position]))
                visited.add(next_position)

    return None  # Если путь не найден

# Пример использования
maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]
start = (0, 0)
end = (4, 4)

path = bfs_maze(maze, start, end)
if path:
    print("\nПуть в лабиринте BFS:", path)
else:
    print("\nПуть не найден")