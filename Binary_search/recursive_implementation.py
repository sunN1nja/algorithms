def binary_search_recursive(arr, target, left, right):
    """
    Рекурсивная функция бинарного поиска.

    :param arr: Отсортированный список элементов, в котором выполняется поиск.
    :param target: Искомое значение.
    :param left: Левый индекс текущего подмассива.
    :param right: Правый индекс текущего подмассива.
    :return: Индекс искомого значения, если оно найдено, иначе -1.
    """
    if left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return binary_search_recursive(arr, target, mid + 1, right)
        else:
            return binary_search_recursive(arr, target, left, mid - 1)

    return -1

# Пример использования
arr = [3, 9, 10, 27, 38, 43, 82]
target = 43

result = binary_search_recursive(arr, target, 0, len(arr) - 1)
if result != -1:
    print(f"Элемент найден на индексе: {result}")
else:
    print("Элемент не найден")