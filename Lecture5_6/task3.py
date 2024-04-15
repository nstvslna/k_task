def reverse_string(s):
    if len(s) <= 1:
        return s

    return s[-1] + reverse_string(s[:-1])


input_string = input("Введіть рядок для реверсу: ")
reversed_string = reverse_string(input_string)
print("Реверс рядка:", reversed_string)
