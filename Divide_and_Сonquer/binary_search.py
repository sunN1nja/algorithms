def binary_search(arr, target):
    return binary_search_recursive(arr, target, 0, len(arr) - 1)

def binary_search_recursive(arr, target, left, right):
    if left > right:
        return -1  # Элемент не найден
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)

# Пример использования
arr = [2, 3, 4, 10, 40]
target = 10
index = binary_search(arr, target)
if index != -1:
    print(f"Элемент найден на индексе {index}")  # Вывод: Элемент найден на индексе 3
else:
    print("Элемент не найден")