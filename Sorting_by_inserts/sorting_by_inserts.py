def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        # Перемещаем элементы arr[0..i-1], которые больше ключа, на одну позицию вперед
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Пример использования
if __name__ == "__main__":
    sample_array = [64, 25, 12, 22, 11]
    print("Исходный массив:", sample_array)
    insertion_sort(sample_array)
    print("Отсортированный массив:", sample_array)