def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    # Подсчет количества элементов для текущего разряда
    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    # Преобразование count для хранения фактических позиций в output
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Построение output массива
    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    # Копирование output в arr
    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    # Нахождение максимального числа для определения количества разрядов
    max_num = max(arr)

    # Применение counting_sort для каждого разряда
    exp = 1
    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

# Пример использования
arr = [170, 45, 75, 90, 802, 24, 2, 66]
print("Исходный массив:", arr)
radix_sort(arr)
print("Отсортированный массив:", arr)