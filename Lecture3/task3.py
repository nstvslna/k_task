def check_happy_ticket(ticket_number):
    if len(ticket_number) != 6:
        return "Невірний формат номера"

    # Розбиваємо рядок на список цифр
    digits = [int(digit) for digit in ticket_number]

    # Обчислюємо суми перших та останніх трьох цифр
    first_sum = sum(digits[:3])
    second_sum = sum(digits[3:])

    # Порівнюємо суми
    if first_sum == second_sum:
        return "Щасливий"
    else:
        return "Звичайний"

ticket_number = input("Введіть номер квитка (шість цифр): ")
result = check_happy_ticket(ticket_number)
print(result)
