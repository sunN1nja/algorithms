def reverse_string(s):
    stack = Stack()
    for char in s:
        stack.push(char)

    reversed_string = ''
    while not stack.is_empty():
        reversed_string += stack.pop()

    return reversed_string

# Пример использования
input_string = "hello"
print(reverse_string(input_string))  # Вывод: "olleh"