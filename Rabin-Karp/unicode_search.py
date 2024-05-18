text = "Привет, мир! Привет, Python!"
pattern = "Привет"
positions = rabin_karp_search_all(text, pattern)
print(f"Подстрока найдена в позициях: {positions}")  # Вывод: [0, 13]