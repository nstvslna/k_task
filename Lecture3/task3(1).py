def check_happy_ticket(ticket_number):
    if len(ticket_number) != 6:
        return "Невірний формат номера"

    ticket_number = int(ticket_number)

    first_half_sum = (ticket_number // 100000) % 10 + (ticket_number // 10000) % 10 + (ticket_number // 1000) % 10
    second_half_sum = (ticket_number // 100) % 10 + (ticket_number // 10) % 10 + (ticket_number // 1) % 10

    if first_half_sum == second_half_sum:
        return "Щасливий"
    else:
        return "Звичайний"

# Приклад використання
ticket_number = input("Введіть номер квитка (шість цифр): ")
result = check_happy_ticket(ticket_number)
print(result)
