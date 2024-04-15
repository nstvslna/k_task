def reverse_sequence():
    num = int(input("Введіть число: "))

    if num != 0:
        reverse_sequence()
    print(num, end=' ')


reverse_sequence()
