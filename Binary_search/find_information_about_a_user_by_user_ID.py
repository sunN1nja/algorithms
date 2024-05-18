def find_user_by_id(users, user_id):
    """
    Функция для поиска пользователя по идентификатору с использованием бинарного поиска.

    :param users: Отсортированный список пользователей, где каждый пользователь представлен словарем с ключом 'id'.
    :param user_id: Идентификатор искомого пользователя.
    :return: Словарь с данными пользователя, если он найден, иначе None.
    """
    left, right = 0, len(users) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if users[mid]['id'] == user_id:
            return users[mid]
        elif users[mid]['id'] < user_id:
            left = mid + 1
        else:
            right = mid - 1

    return None

# Пример использования
users = [
    {'id': 1, 'name': 'Alice'},
    {'id': 2, 'name': 'Bob'},
    {'id': 3, 'name': 'Charlie'},
    {'id': 4, 'name': 'David'},
    {'id': 5, 'name': 'Eve'}
]

user_id = 3
result = find_user_by_id(users, user_id)
if result:
    print(f"Пользователь найден: {result}")
else:
    print("Пользователь не найден")