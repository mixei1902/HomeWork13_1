class Product:
    name: str
    description: str
    price: float
    quantity: list

    def __init__(self, name: str, description: str, price: float, quantity: list):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
