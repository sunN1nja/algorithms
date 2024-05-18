def is_connected(graph, start):
    visited = set()
    dfs_recursive(graph, start, visited)
    return len(visited) == len(graph)

# Пример использования
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

print("\nГраф связен:", is_connected(graph, 'A'))