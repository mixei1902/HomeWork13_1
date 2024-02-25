class Category:
    name: str
    description: str
    products: list
    total_categories = 0
    total_unique_products = 0

    def __init__(self, name: str, description: str, products: list):
        self.name = name
        self.description = description
        self.products = products if products else []
        Category.total_categories += 1
        Category.total_unique_products += len(products)

    def add_product(self, product):
        self.products.append(product)
        Category.total_unique_products += 1

    @property
    def products(self):
        return "\n".join(
            [f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт." for product in self.products])

    @products.setter
    def products(self, value):
        self._products = value
