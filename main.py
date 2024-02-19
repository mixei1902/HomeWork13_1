class Category:
    total_categories = 0
    total_unique_products = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products
        Category.total_categories += 1
        Category.total_unique_products += len(products)

class Product:
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


