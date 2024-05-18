def heapify(arr, n, i):
    largest = i  # Инициализируем наибольший элемент как корень
    left = 2 * i + 1  # Левый = 2*i + 1
    right = 2 * i + 2  # Правый = 2*i + 2

    # Если левый дочерний элемент больше корня
    if left < n and arr[i] < arr[left]:
        largest = left

    # Если правый дочерний элемент больше, чем самый большой элемент на данный момент
    if right < n and arr[largest] < arr[right]:
        largest = right

    # Если самый большой элемент не корень
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Меняем местами

        # Рекурсивно преобразуем в куче затронутое поддерево
        heapify(arr, n, largest)

def heapsort(arr):
    n = len(arr)

    # Построение кучи (перегруппируем массив)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Один за другим извлекаем элементы из кучи
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Меняем текущий корень с концом
        heapify(arr, i, 0)

# Пример использования
arr = [12, 11, 13, 5, 6, 7]
heapsort(arr)
print("Sorted array is:", arr)  # Вывод: [5, 6, 7, 11, 12, 13]