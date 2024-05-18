def hash_function(s, prime=101):
    hash_value = 0
    for i, char in enumerate(s):
        hash_value += ord(char) * (prime ** i)
    return hash_value