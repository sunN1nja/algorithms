import hashlib

# Пример 1: Вычисление хеша строки
def calculate_hash(input_string):
    hash_object = hashlib.sha256(input_string.encode())
    hex_dig = hash_object.hexdigest()
    return hex_dig

input_data = "Hello, World!"
hashed_value = calculate_hash(input_data)
print(f"Хеш для '{input_data}': {hashed_value}")

# Пример 2: Хеширование паролей
def hash_password(password):
    salt = b'salt_'
    hash_object = hashlib.sha256(salt + password.encode())
    hex_dig = hash_object.hexdigest()
    return hex_dig

password = "password123"
hashed_password = hash_password(password)
print(f"Хеш пароля '{password}': {hashed_password}")