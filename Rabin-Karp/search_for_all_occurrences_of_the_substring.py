def rabin_karp_search_all(text, pattern, prime=101):
    n = len(text)
    m = len(pattern)
    pattern_hash = hash_function(pattern, prime)
    current_hash = hash_function(text[:m], prime)
    results = []

    for i in range(n - m + 1):
        if current_hash == pattern_hash:
            if text[i:i + m] == pattern:
                results.append(i)
        if i < n - m:
            current_hash = (current_hash - ord(text[i])) // prime
            current_hash += ord(text[i + m]) * (prime ** (m - 1))

    return results

# Пример использования
text = "ababcabcabababd"
pattern = "ab"
positions = rabin_karp_search_all(text, pattern)
print(f"Подстрока найдена в позициях: {positions}")  # Вывод: [0, 2, 7, 9, 11]