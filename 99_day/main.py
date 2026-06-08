# Shopping Cart System
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity

    def display_product(self):
        print("Product:", self.name)
        print("Price:", self.price)
        print("Quantity:", self.quantity)
        print("Total:", self.calculate_total_price())


class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_product(self, product):
        self.items.append(product)

    def calculate_cart_total(self):
        total = 0
        for product in self.items:
            total += product.calculate_total_price()
        return total

    def display_cart(self):
        print("Shopping Cart")
        print("-" * 20)
        for product in self.items:
            product.display_product()
            print("-" * 20)
        print("Cart Total:", self.calculate_cart_total())


cart = ShoppingCart()
cart.add_product(Product("Laptop", 55000, 1))
cart.add_product(Product("Mouse", 700, 2))
cart.add_product(Product("Keyboard", 1500, 1))
cart.display_cart()