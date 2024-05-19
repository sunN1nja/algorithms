class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash(key)
        for kv in self.table[index]:
            if kv[0] == key:
                kv[1] = value
                return
        self.table[index].append([key, value])

    def search(self, key):
        index = self._hash(key)
        for kv in self.table[index]:
            if kv[0] == key:
                return kv[1]
        return None

    def delete(self, key):
        index = self._hash(key)
        for i, kv in enumerate(self.table[index]):
            if kv[0] == key:
                del self.table[index][i]
                return

# Пример использования
ht = HashTable()
ht.insert("apple", 1)
ht.insert("banana", 2)
ht.insert("orange", 3)

print(ht.search("apple"))  # Вывод: 1
print(ht.search("banana"))  # Вывод: 2

ht.delete("apple")
print(ht.search("apple"))  # Вывод: None