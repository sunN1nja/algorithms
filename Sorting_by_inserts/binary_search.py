def binary_insertion_sort(arr):
    def binary_search(sub_arr, val, start, end):
        if start == end:
            if sub_arr[start] > val:
                return start
            else:
                return start + 1
        if start > end:
            return start

        mid = (start + end) // 2
        if sub_arr[mid] < val:
            return binary_search(sub_arr, val, mid + 1, end)
        elif sub_arr[mid] > val:
            return binary_search(sub_arr, val, start, mid - 1)
        else:
            return mid

    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = binary_search(arr, key, 0, i - 1)
        arr = arr[:j] + [key] + arr[j:i] + arr[i + 1:]
    return arr

# Пример использования
if __name__ == "__main__":
    sample_array = [64, 25, 12, 22, 11]
    print("Исходный массив:", sample_array)
    sorted_array = binary_insertion_sort(sample_array)
    print("Отсортированный массив:", sorted_array)