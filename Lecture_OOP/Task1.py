class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_info(self):
        return f"Name: {self.name}, Price: {self.price}, Quantity: {self.quantity}"


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email


class Administrator(User):
    def view_order(self, order):
        print(f"Order by {order.client.name}:")
        for product in order.products:
            print(product.get_info())
        print(f"Total amount: {order.calculate_total()}")


class Order:
    def __init__(self, client):
        self.client = client
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        self.products.remove(product)

    def calculate_total(self):
        return sum(product.price for product in self.products)


class Cart:
    def __init__(self):
        self.products = {}

    def add_product(self, product, quantity):
        if product.name in self.products:
            self.products[product.name].quantity += quantity
        else:
            self.products[product.name] = Product(product.name, product.price, quantity)

    def remove_product(self, product):
        if product.name in self.products:
            del self.products[product.name]

    def clear_cart(self):
        self.products = {}

    def get_cart_info(self):
        info = []
        for product in self.products.values():
            info.append(product.get_info())
        return "\n".join(info)


# Example usage
product1 = Product("Laptop", 1000, 10)
product2 = Product("Mouse", 50, 200)
user = User("John Doe", "john@gmail.com")
admin = Administrator("Admin", "admin@gmail.com")

order = Order(user)
order.add_product(product1)
order.add_product(product2)

cart = Cart()
cart.add_product(product1, 2)
cart.add_product(product2, 5)

print("Cart info:")
print(cart.get_cart_info())

admin.view_order(order)
