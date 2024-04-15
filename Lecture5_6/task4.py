def shorten_string(s):
    if len(s) <= 1:
        return s
    else:
        # Якщо перший і останній символи рівні, видаляємо їх та рекурсивно викликаємо функцію для решти рядка
        if s[0] == s[-1]:
            return shorten_string(s[1:-1])
        else:
            # Якщо перший і останній символи не рівні, повертаємо перший символ та рекурсивно викликаємо функцію для решти рядка
            return s[0] + shorten_string(s[1:-1]) + s[-1]

# Приклад використання:
input_string = "pythontip"
shortened_string = shorten_string(input_string)
print("Скорочений рядок:", shortened_string)
