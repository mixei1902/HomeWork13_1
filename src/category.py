from src.product import Product


class ZeroQuantityError(ValueError):
    """ Класс исключения для товаров с нулевым количеством """
    def __init__(self, message='Товар не может быть добавлен'):
        self.message = message
        super().__init__(self.message)


class Category:
    """ Класс категории товаров """
    name: str
    description: str
    products: list
    total_categories = 0
    total_unique_products = 0

    def __init__(self, name: str, description: str, products: list):
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.total_categories += 1
        Category.total_unique_products += len(self.__products)

    def add_product(self, product):
        if isinstance(product, Product):
            if product.quantity == 0:
                raise ZeroQuantityError  # вызывается, когда добавить товар с нулевым количеством в категорию
            self.__products.append(product)
            Category.total_unique_products += 1
        else:
            raise TypeError("Можно добавить только экземпляры класса Product или его подклассов.")

    def average_price(self):
        """
        Возвращает среднюю цену всех товаров в категории.
        Если в категории нет товаров, этот метод возвращает 0.
        """
        try:
            total_price = sum(product.price for product in self.__products)
            return total_price / len(self.__products)
        except ZeroDivisionError:
            return 0

    @property
    def products(self):
        return "\n".join(
            [f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт." for product in self.__products])

    @property
    def product_list(self):
        return self.__products

    @products.setter
    def products(self, value):
        self.__products = value

    def __str__(self):
        return f"{self.name}, количество продуктов: {Category.total_unique_products} шт."
