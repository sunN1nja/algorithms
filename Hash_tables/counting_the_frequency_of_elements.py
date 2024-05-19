def count_frequency(arr):
    freq_table = {}
    for item in arr:
        if item in freq_table:
            freq_table[item] += 1
        else:
            freq_table[item] = 1
    return freq_table

# Пример использования
arr = ["apple", "banana", "apple", "orange", "banana", "apple"]
frequency = count_frequency(arr)
print(frequency)  # Вывод: {'apple': 3, 'banana': 2, 'orange': 1}