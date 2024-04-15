def is_palindrome(s):
    if not isinstance(s, str):
        raise ValueError("Input must be a string")

    start_index, end_index = 0, len(s) - 1

    while start_index < end_index:
        start_char, end_char = s[start_index], s[end_index]

        if not start_char.isalpha():
            start_index += 1
            continue
        if not end_char.isalpha():
            end_index -= 1
            continue

        if start_char.lower() != end_char.lower():
            return False

        start_index += 1
        end_index -= 1

    return True


# Приклад
print(is_palindrome("A man, a plan, a canal, Panama"))  # True
print(is_palindrome("Was it a car or a cat I saw?"))  # True
print(is_palindrome("Hello, world!"))  # False
