def binary_search_iterative(arr, target):
    """
    Итеративная функция бинарного поиска.

    :param arr: Отсортированный список элементов, в котором выполняется поиск.
    :param target: Искомое значение.
    :return: Индекс искомого значения, если оно найдено, иначе -1.
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

# Пример использования
arr = [3, 9, 10, 27, 38, 43, 82]
target = 43

result = binary_search_iterative(arr, target)
if result != -1:
    print(f"Элемент найден на индексе: {result}")
else:
    print("Элемент не найден")