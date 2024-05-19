def merge_sort(arr):
    if len(arr) > 1:
        # Разделяем массив на две половины
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Рекурсивно сортируем каждую половину
        merge_sort(left_half)
        merge_sort(right_half)

        # Индексы для левой, правой половин и основного массива
        i = j = k = 0

        # Слияние отсортированных половин
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Копируем оставшиеся элементы левой половины, если есть
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Копируем оставшиеся элементы правой половины, если есть
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Пример использования
arr = [38, 27, 43, 3, 9, 82, 10]
print("Исходный массив:", arr)
merge_sort(arr)
print("Отсортированный массив:", arr)