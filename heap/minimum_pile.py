import heapq

# Создание пустой кучи
min_heap = []

# Вставка элементов
heapq.heappush(min_heap, 3)
heapq.heappush(min_heap, 1)
heapq.heappush(min_heap, 4)
heapq.heappush(min_heap, 1)
heapq.heappush(min_heap, 5)

print("Min-Heap:", min_heap)  # Вывод: [1, 1, 4, 3, 5]

# Извлечение минимального элемента
min_element = heapq.heappop(min_heap)
print("Extracted Min:", min_element)  # Вывод: 1
print("Min-Heap after extraction:", min_heap)  # Вывод: [1, 3, 4, 5]