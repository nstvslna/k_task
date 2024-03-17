def calculator(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '/':
        if num2 == 0:
            return "Ділення на 0 неможливе!"
        else:
            return num1 / num2
    elif operator == '*':
        return num1 * num2
    elif operator == 'mod':
        return num1 % num2
    elif operator == 'pow':
        return pow(num1, num2)
    elif operator == 'div':
        return num1 // num2
    else:
        return "Недійсний оператор"


num1 = float(input())
operator = input()
num2 = float(input())

result = calculator(num1, num2, operator)
print("Результат", result)
