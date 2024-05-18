import heapq

class PriorityQueue:
    def __init__(self):
        self.heap = []

    def push(self, item, priority):
        heapq.heappush(self.heap, (priority, item))

    def pop(self):
        return heapq.heappop(self.heap)[1]

    def is_empty(self):
        return len(self.heap) == 0

# Пример использования
pq = PriorityQueue()
pq.push("task1", 1)
pq.push("task2", 3)
pq.push("task3", 2)

while not pq.is_empty():
    print(pq.pop())
# Вывод:
# task1
# task3
# task2