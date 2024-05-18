class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value
        self.ratio = value / weight

def fractional_knapsack(weights, values, W):
    """
    Решение дробной задачи о рюкзаке с использованием жадного алгоритма.

    :param weights: Список весов предметов.
    :param values: Список стоимостей предметов.
    :param W: Максимальный вес рюкзака.
    :return: Максимальная стоимость, которую можно получить.
    """
    items = [Item(weights[i], values[i]) for i in range(len(weights))]
    items.sort(key=lambda x: x.ratio, reverse=True)

    total_value = 0
    for item in items:
        if W >= item.weight:
            W -= item.weight
            total_value += item.value
        else:
            total_value += item.value * (W / item.weight)
            break

    return total_value

# Пример использования
weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
W = 5

max_value = fractional_knapsack(weights, values, W)
print(f"Максимальная стоимость, которую можно получить: {max_value}")