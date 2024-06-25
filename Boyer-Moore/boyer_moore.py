def preprocess_bad_character(pattern):
    bad_char_table = {}
    for i in range(len(pattern) - 1):
        bad_char_table[pattern[i]] = i
    return bad_char_table

def preprocess_good_suffix(pattern):
    m = len(pattern)
    good_suffix_table = [0] * (m + 1)
    z = [0] * m
    z[m - 1] = m
    l, r = m - 1, m - 1
    for i in range(m - 2, -1, -1):
        if i > l and z[i + m - 1 - r] < i - l:
            z[i] = z[i + m - 1 - r]
        else:
            if i < l:
                l = i
            r = i
            while l >= 0 and pattern[l] == pattern[l + m - 1 - r]:
                l -= 1
            z[i] = r - l
    for i in range(m - 1):
        good_suffix_table[m - z[i]] = i
    l = 0
    for i in range(m - 1, -1, -1):
        if z[i] == i + 1:
            for j in range(l, m - i - 1):
                if good_suffix_table[j] == 0:
                    good_suffix_table[j] = m - i - 1
            l = m - i - 1
    return good_suffix_table

def boyer_moore(text, pattern):
    n = len(text)
    m = len(pattern)
    if m == 0:
        return []

    bad_char_table = preprocess_bad_character(pattern)
    good_suffix_table = preprocess_good_suffix(pattern)
    
    i = 0
    result = []
    while i <= n - m:
        j = m - 1
        while j >= 0 and pattern[j] == text[i + j]:
            j -= 1
        if j < 0:
            result.append(i)
            i += good_suffix_table[0] if good_suffix_table[0] > 0 else 1
        else:
            bad_char_shift = j - bad_char_table.get(text[i + j], -1)
            good_suffix_shift = good_suffix_table[j + 1]
            i += max(bad_char_shift, good_suffix_shift)
    return result

# Пример использования
text = "ABAAABCD"
pattern = "ABC"
positions = boyer_moore(text, pattern)
print("Pattern found at positions:", positions)