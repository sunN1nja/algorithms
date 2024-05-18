import heapq

# Создание пустой кучи
max_heap = []

# Вставка элементов (инвертирование значений)
heapq.heappush(max_heap, -3)
heapq.heappush(max_heap, -1)
heapq.heappush(max_heap, -4)
heapq.heappush(max_heap, -1)
heapq.heappush(max_heap, -5)

print("Max-Heap (inverted):", max_heap)  # Вывод: [-5, -3, -4, -1, -1]

# Извлечение максимального элемента (инвертирование значения обратно)
max_element = -heapq.heappop(max_heap)
print("Extracted Max:", max_element)  # Вывод: 5
print("Max-Heap after extraction (inverted):", max_heap)  # Вывод: [-4, -3, -1, -1]