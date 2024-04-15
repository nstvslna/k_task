def get_longest_word(s: str) -> str:
    if not isinstance(s, str):
        raise ValueError("Input must be a string")

    words = s.split()
    longest_word = max(words, key=len)
    return longest_word


print(get_longest_word('Python is simple and effective!'))
print(get_longest_word('Any pythonista like namespaces a lot.'))
