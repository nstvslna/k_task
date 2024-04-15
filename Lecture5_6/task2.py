def is_palindrome(s):
    # Якщо рядок має довжину 0 або 1, то він є паліндромом
    if len(s) <= 1:
        return True
    # Перевіряємо перший і останній символи рядка
    if s[0] != s[-1]:
        return False
    # Рекурсивний виклик для підстроки без першого і останнього символів
    return is_palindrome(s[1:-1])


input_string = input("Введіть рядок для перевірки на паліндром: ")
if is_palindrome(input_string):
    print("Це паліндром!")
else:
    print("Це не паліндром.")
