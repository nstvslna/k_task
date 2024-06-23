class Employee:
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary
        self.__bonus = 0

    @property
    def name(self):
        return self.__name

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        self.__salary = value

    def set_bonus(self, bonus):
        self.__bonus = bonus

    def to_pay(self):
        return self.__salary + self.__bonus


class SalesPerson(Employee):
    def __init__(self, name, salary, percent):
        super().__init__(name, salary)
        self.__percent = percent

    def set_bonus(self, bonus):
        if self.__percent > 100:
            bonus *= 2
        elif self.__percent > 200:
            bonus *= 3
        super().set_bonus(bonus)


class Manager(Employee):
    def __init__(self, name, salary, quantity):
        super().__init__(name, salary)
        self.__quantity = quantity

    def set_bonus(self, bonus):
        if self.__quantity > 100:
            bonus += 500
        elif self.__quantity > 150:
            bonus += 1000
        super().set_bonus(bonus)


class Company:
    def __init__(self, employees):
        self.__employees = employees

    def give_everybody_bonus(self, company_bonus: float):
        for employee in self.__employees:
            employee.set_bonus(company_bonus)

    def total_to_pay(self):
        total_salary = 0
        for employee in self.__employees:
            total_salary += employee.to_pay()
        return total_salary

    def name_max_salary(self) -> str:
        max_salary = 0
        max_salary_employee = None
        for employee in self.__employees:
            current_salary = employee.to_pay()
            if current_salary > max_salary:
                max_salary = current_salary
                max_salary_employee = employee
        if max_salary_employee:
            return max_salary_employee.name


def input_employee_data():
    employees = []
    while True:
        name = input("Введіть прізвище працівника: ")
        salary = float(input("Введіть зарплату працівника: "))
        employee_type = input("Введіть тип працівника (SalesPerson, Manager): ")

        if employee_type == "SalesPerson":
            percent = float(input("Введіть відсоток виконання плану продажів: "))
            emp = SalesPerson(name, salary, percent)
        elif employee_type == "Manager":
            client_amount = int(input("Введіть кількість обслуговуваних клієнтів: "))
            emp = Manager(name, salary, client_amount)
        else:
            emp = Employee(name, salary)

        employees.append(emp)

        add_another = input("Хочете додати ще одного співробітника? (так/ні): ")
        if add_another.lower() != "так":
            break

    return employees


employees = input_employee_data()

company = Company(employees)

company_bonus = float(input("Введіть розмір основного бонусу для кожного співробітника: "))
company.give_everybody_bonus(company_bonus)

print("Загальна сума заробітної плати всіх співробітників:", company.total_to_pay())
print("Прізвище співробітника, який отримав максимальну зарплату з бонусом:", company.name_max_salary())
