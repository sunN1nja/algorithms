def cover_segments(segments):
    segments.sort(key=lambda x: x[1])
    result = []
    current_end = -float('inf')
    for segment in segments:
        if segment[0] > current_end:
            current_end = segment[1]
            result.append(segment)
    return result

# Пример использования
segments = [(1, 3), (2, 5), (3, 6)]
result = cover_segments(segments)
print(f"Минимальное количество отрезков для покрытия: {result}")
# Вывод: [(1, 3), (3, 6)]