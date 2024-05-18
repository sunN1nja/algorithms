def rabin_karp_search_case_insensitive(text, pattern, prime=101):
    text = text.lower()
    pattern = pattern.lower()
    return rabin_karp_search_all(text, pattern, prime)

# Пример использования
text = "AbAbCaBcAbAbAbD"
pattern = "ab"
positions = rabin_karp_search_case_insensitive(text, pattern)
print(f"Подстрока найдена в позициях: {positions}")  # Вывод: [0, 2, 7, 9, 11]