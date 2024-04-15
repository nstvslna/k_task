def custom_split(string, delimiter=None):
    if not isinstance(string, str):
        raise ValueError("Input must be a string")

    if delimiter is None:
        delimiter = ' '

    result = []
    current_word = ''

    for char in string:
        if char == delimiter:
            if current_word:
                result.append(current_word)
                current_word = ''
        else:
            current_word += char

    # Додаємо останнє слово, якщо воно є
    if current_word:
        result.append(current_word)

    return result


# Приклад
sentence = "Це простий текст, щоб розділити."
print(custom_split(sentence))  # ['Це', 'простий', 'текст,', 'щоб', 'розділити.']
print(custom_split(sentence, ','))  # ['Це простий текст', ' щоб розділити.']
