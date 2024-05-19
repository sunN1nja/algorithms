class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("pop from empty stack")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("peek from empty stack")

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

# Пример использования
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.pop())  # Вывод: 3
print(stack.peek())  # Вывод: 2
print(stack.size())  # Вывод: 2
print(stack.is_empty())  # Вывод: False