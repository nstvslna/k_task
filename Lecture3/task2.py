def men(a):
    if a == 1 or a % 10 == 1:
        print(f"{a} програміст")
    elif a % 10 == 2 or a % 10 == 3 or a % 10 == 4:
        print(f"{a} програміста")
    else:
        print(f"{a} програмістів")


a = int(input("Введіть кількість студентів: "))
if a < 0:
    print("Введіть додатне число!")

men(a)
