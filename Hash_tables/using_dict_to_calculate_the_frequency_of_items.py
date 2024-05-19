arr = ["apple", "banana", "apple", "orange", "banana", "apple"]
frequency = {}

for item in arr:
    if item in frequency:
        frequency[item] += 1
    else:
        frequency[item] = 1

print(frequency)  # Вывод: {'apple': 3, 'banana': 2, 'orange': 1}