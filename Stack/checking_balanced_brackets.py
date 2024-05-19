def is_balanced(expression):
    stack = Stack()
    pairs = {')': '(', ']': '[', '}': '{'}
    
    for char in expression:
        if char in pairs.values():
            stack.push(char)
        elif char in pairs.keys():
            if stack.is_empty() or stack.pop() != pairs[char]:
                return False

    return stack.is_empty()

# Пример использования
expression = "{[()()]}"
print(is_balanced(expression))  # Вывод: True

expression = "{[(])}"
print(is_balanced(expression))  # Вывод: False