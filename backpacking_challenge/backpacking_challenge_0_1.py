def knapsack(weights, values, W):
    """
    Решение задачи о рюкзаке с использованием динамического программирования.

    :param weights: Список весов предметов.
    :param values: Список стоимостей предметов.
    :param W: Максимальный вес рюкзака.
    :return: Максимальная стоимость, которую можно получить.
    """
    n = len(weights)
    dp = [[0] * (W + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(W + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-weights[i-1]] + values[i-1])
            else:
                dp[i][w] = dp[i-1][w]
    
    return dp[n][W]

# Пример использования
weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
W = 5

max_value = knapsack(weights, values, W)
print(f"Максимальная стоимость, которую можно получить: {max_value}")