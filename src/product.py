from abc import ABC, abstractmethod


class LoggableMixin:
    """ Миксин для вывода информации о создании объекта """
    def __repr__(self):
        attrs = ", ".join(f"{k}={v}" for k, v in self.__dict__.items())
        return f"{self.__class__.__name__}({attrs})"


class AbstractProduct(ABC, LoggableMixin):
    """ Абстрактный класс продукта """
    @abstractmethod
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        print(self)

    @abstractmethod
    def __add__(self, other):
        pass


class Product(AbstractProduct):
    """ Класс катеогрии продуктов """
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int):
        super().__init__(name, description, price, quantity)

    @classmethod
    def create_product(cls, name: str, description: str, price: float, quantity: int):
        return cls(name, description, price, quantity)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value: int):
        if value <= 0:
            print("Цена введена некорректная")
        else:
            self.__price = value

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """ складывает товары только из одинаковых классов продуктов """
        if type(self) == type(other):
            return self.price * self.quantity + other.price * other.quantity
        return NotImplemented


class Smartphone(Product):
    """ Подкласс для продуктов типа Смартфон """
    def __init__(self, name: str, description: str, price: float, quantity: int, performance: str, model: str,
                 memory: int, color: str):
        super().__init__(name, description, price, quantity)
        self.performance = performance
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    """ Подкласс для продуктов типа Трава газонная """
    def __init__(self, name: str, description: str, price: float, quantity: int, country: str, germination_period: str,
                 color: str):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

