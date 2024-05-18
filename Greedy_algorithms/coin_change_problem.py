def coin_change(coins, amount):
    coins.sort(reverse=True)
    result = []
    for coin in coins:
        while amount >= coin:
            amount -= coin
            result.append(coin)
    return result

# Пример использования
coins = [1, 5, 10, 25]
amount = 63
result = coin_change(coins, amount)
print(f"Минимальное количество монет для суммы {amount}: {result}")  # Вывод: [25, 25, 10, 1, 1, 1]