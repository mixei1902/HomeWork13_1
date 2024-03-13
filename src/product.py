from abc import ABC, abstractmethod


class LoggableMixin:
    """ Миксин для вывода информации о создании объекта """

    def __init__(self):
        print(repr(self))

    def __repr__(self):
        attrs = ", ".join(f"{k}={v}" for k, v in vars(self).items())
        return f"{self.__class__.__name__}({attrs})"


class AbstractProduct(ABC):
    """ Абстрактный класс продукта """

    @abstractmethod
    def __init__(self, name: str, description: str, price: float, quantity: int):
        pass

    @classmethod
    @abstractmethod
    def create_product(cls, *args, **kwargs):
        pass

    @abstractmethod
    def __add__(self, other):
        pass


class Product(LoggableMixin, AbstractProduct):
    """ Класс катеогрии продуктов """
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
        super().__init__()

    @classmethod
    def create_product(cls, name: str, description: str, price: float, quantity: int):
        return cls(name, description, price, quantity)

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value: int):
        if value <= 0:
            print("Цена введена некорректная")
        else:
            self._price = value

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """ Складывает товары только из одинаковых классов продуктов """
        if type(self) == type(other):
            return self.price * self.quantity + other.price * other.quantity
        raise TypeError("не одинаковый класс продукта!")


class Smartphone(Product):
    """ Подкласс для продуктов типа Смартфон """

    def __init__(self, name: str, description: str, price: float, quantity: int, performance: str, model: str,
                 memory: int, color: str):
        self.performance = performance
        self.model = model
        self.memory = memory
        self.color = color
        super().__init__(name, description, price, quantity)

    @classmethod
    def create_product(cls, name: str, description: str, price: float, quantity: int, performance: str, model: str,
                       memory: int, color: str):
        return cls(name, description, price, quantity, performance, model, memory, color)
    #получается тест только если переопределить метод create_product

class LawnGrass(Product):
    """ Подкласс для продуктов типа Трава газонная """

    def __init__(self, name: str, description: str, price: float, quantity: int, country: str, germination_period: str,
                 color: str):
        self.country = country
        self.germination_period = germination_period
        self.color = color
        super().__init__(name, description, price, quantity)

    @classmethod
    def create_product(cls, name: str, description: str, price: float, quantity: int, country: str, germination_period: str,
                 color: str):
        return cls(name, description, price, quantity, country, germination_period, color)
