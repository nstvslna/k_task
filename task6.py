import sys


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
  else:
    return "Недійсний оператор"


num1 = float(sys.argv[1])
operator = sys.argv[2]
num2 = float(sys.argv[3])

result = calculator(num1, num2, operator)
print("Результат", result)
