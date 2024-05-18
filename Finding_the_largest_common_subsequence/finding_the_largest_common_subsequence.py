def lcs(X, Y):
    """
    Решение задачи поиска наибольшей общей подпоследовательности с использованием динамического программирования.

    :param X: Первая последовательность.
    :param Y: Вторая последовательность.
    :return: Длина наибольшей общей подпоследовательности и сама подпоследовательность.
    """
    m = len(X)
    n = len(Y)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Заполнение таблицы dp
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i-1] == Y[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    # Реконструкция наибольшей общей подпоследовательности
    lcs_length = dp[m][n]
    lcs_sequence = []
    i, j = m, n
    while i > 0 and j > 0:
        if X[i-1] == Y[j-1]:
            lcs_sequence.append(X[i-1])
            i -= 1
            j -= 1
        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1
    
    lcs_sequence.reverse()
    return lcs_length, ''.join(lcs_sequence)

# Пример использования
X = "AGGTAB"
Y = "GXTXAYB"

lcs_length, lcs_sequence = lcs(X, Y)
print(f"Длина наибольшей общей подпоследовательности: {lcs_length}")
print(f"Наибольшая общая подпоследовательность: {lcs_sequence}")