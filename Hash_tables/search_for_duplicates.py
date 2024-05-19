def find_duplicates(arr):
    seen = set()
    duplicates = set()
    for item in arr:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    return duplicates

# Пример использования
arr = ["apple", "banana", "apple", "orange", "banana", "grape"]
duplicates = find_duplicates(arr)
print(duplicates)  # Вывод: {'apple', 'banana'}