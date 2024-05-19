def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Флаг для оптимизации: если на текущем проходе не было обменов, массив уже отсортирован
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        # Если не было обменов, завершить сортировку
        if not swapped:
            break

# Пример использования
if __name__ == "__main__":
    sample_array = [64, 34, 25, 12, 22, 11, 90]
    print("Исходный массив:", sample_array)
    bubble_sort(sample_array)
    print("Отсортированный массив:", sample_array)