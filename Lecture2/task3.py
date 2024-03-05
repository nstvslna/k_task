quote = ("The reasonable man adapts himself to the world; the unreasonable one persists in tryingto adapt the world to "
         "himself.")

# Розділити цитату на список слів
words = quote.split()

# Знаходимо індекс слів "reasonable" і "unreasonable"
index_reasonable = words.index("reasonable")
index_unreasonable = words.index("unreasonable")

# Змінюємо позиції
words[index_reasonable], words[index_unreasonable] = words[index_unreasonable], words[index_reasonable]

# Об'єднуємо список в рядок
new_quote = " ".join(words)

print(new_quote)
