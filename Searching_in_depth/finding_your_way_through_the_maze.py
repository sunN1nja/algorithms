def dfs_maze(maze, start, end, path=None):
    if path is None:
        path = []
    
    x, y = start
    if not (0 <= x < len(maze) and 0 <= y < len(maze[0])) or maze[x][y] == 1:
        return False

    path.append(start)
    if start == end:
        return True

    maze[x][y] = 1  # Помечаем ячейку как посещённую

    # Проверяем все соседние ячейки (вверх, вниз, влево, вправо)
    if (dfs_maze(maze, (x + 1, y), end, path) or
        dfs_maze(maze, (x - 1, y), end, path) or
        dfs_maze(maze, (x, y + 1), end, path) or
        dfs_maze(maze, (x, y - 1), end, path)):
        return True

    path.pop()
    return False

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
path = []

if dfs_maze(maze, start, end, path):
    print("\nПуть найден:", path)
else:
    print("\nПуть не найден")