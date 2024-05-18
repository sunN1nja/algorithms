def linear_search(arr, target):
    """
    Функция линейного поиска.

    :param arr: Список элементов, в котором выполняется поиск.
    :param target: Искомое значение.
    :return: Индекс искомого значения, если оно найдено, иначе -1.
    """
    for index, element in enumerate(arr):
        if element == target:
            return index
    return -1

# Пример использования
arr = [38, 27, 43, 3, 9, 82, 10]
target = 43

result = linear_search(arr, target)
if result != -1:
    print(f"Элемент найден на индексе: {result}")
else:
    print("Элемент не найден")