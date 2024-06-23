TASK 1

Створіть програму для інтернет-магазину, яка дозволяє керувати замовленнями. При реалізації використовуйте різні принципи ООП, такі як інкапсуляція, спадкування, поліморфізм та абстракція.

Орієнтовна структура класів для системи керування замовленнями в інтернет-магазині:

Клас "Товар": Поля: назва: рядок, що містить назву товару. ціна: числове значення, вартість товару. кількість: ціле число, кількість одиниць товару на складі. Методи: init(self, назва, ціна, кількість): конструктор класу, ініціалізує поля товару. отримати_інформацію(self): повертає рядок з інформацією про товар (назва, ціна, кількість). Інші методи за необхідності.

Клас "Замовлення": Поля: товари: список об'єктів класу "Товар", які були додані до замовлення. клієнт: об'єкт класу "Користувач", який зробив замовлення. Методи: init(self, клієнт): конструктор класу, ініціалізує поле клієнта та створює пустий список товарів. додати_товар(self, товар): додає товар до замовлення. видалити_товар(self, товар): видаляє товар з замовлення. підрахувати_суму(self): обчислює загальну вартість замовлення. Інші методи за необхідності.

Класи "Користувач" та "Адміністратор":
Клас "Користувач": Поля: ім'я: рядок, ім'я користувача. email: рядок, адреса електронної пошти користувача. Методи: init(self, ім'я, email): конструктор класу, ініціалізує поля користувача. Інші методи за необхідності.
Клас "Адміністратор" (спадкує від класу "Користувач"): Методи: переглянути_замовлення(self, замовлення): виводить інформацію про замовлення.

Клас "Кошик": Поля: товари: словник, де ключ - ідентифікатор товару, значення - об'єкт класу "Товар". Методи: init(self): конструктор класу, ініціалізує порожній словник товарів. додати_товар(self, товар, кількість): додає товар у кошик з певною кількістю. видалити_товар(self, товар): видаляє товар з кошика. очистити_кошик(self): очищує кошик. Інші методи за необхідності.

https://replit.com/@04-22-253stud/TASK1
********************************************************************************************************************
TASK 2
Create classes Employee, SalesPerson, Manager and Company with predefined functionality.

Create basic class Employee and declare following content:
• Attributes – `name` (str), `salary` and `bonus` (int), set with property decorator
• Constructor - parameters `name` and `salary`
• Method `bonus` - sets bonuses to salary, amount of which is delegated as `bonus`
• Method `to_pay` - returns the value of summarized salary and bonus.

Create class SalesPerson as class Employee inheritor and declare within it:
• Constructor with parameters: `name`, `salary`, `percent` – percent of plan performance (int, without the % symbol), first two of which are passed from basic class constructor
• Redefine method of parent class `bonus` in the following way: if the sales person completed the plan more than 100%, their bonus is doubled (is multiplied by 2), and if more than 200% - bonus is tripled (is multiplied by 3)

Create class Manager as Employee class inheritor, and declare within it:
• Constructor with parameters: `name`, `salary` and `client_number` (int, number of served clients), first two of which are passed to basic class constructor.
• Redefine method of parent class `bonus` in the following way: if the manager served over 100 clients, their bonus is increased by 500, and if more than 150 clients – by 1000.

Create class Company and declare within it:
• Constructor with parameters: `employees` – list of company`s employees (made up of Employee/SalesPerson/Manager classes instances) with arbitrary length `n`
• Method `give_everybody_bonus` with parameter company_bonus (int) that sets the amount of basic bonus for each employee.
• Method `total_to_pay` that returns total amount of salary of all employees including awarded bonus
• Method `name_max_salary` that returns name of the employee, who received maximum salary including bonus.

Note:
Class attributes and methods should bear exactly the same names as those given in task description
Methods should return only target values, without detailed explanation within `return`
"""
https://replit.com/@04-22-253stud/TASK2
*************************************************************************************************************************
