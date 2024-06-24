def interpolation_search(arr, key):
    low = 0
    high = len(arr) - 1

    while low <= high and key >= arr[low] and key <= arr[high]:
        if low == high:
            if arr[low] == key:
                return low
            return -1

        pos = low + int(((float(high - low) / (arr[high] - arr[low])) * (key - arr[low])))

        if arr[pos] == key:
            return pos

        if arr[pos] < key:
            low = pos + 1
        else:
            high = pos - 1

    return -1

# Пример использования
arr = [10, 12, 13, 16, 18, 19, 20, 21, 22, 23, 24, 33, 35, 42, 47]
key = 18
index = interpolation_search(arr, key)

if index != -1:
    print(f"Элемент найден в индексе {index}")
else:
    print("Элемент не найден в массиве")
