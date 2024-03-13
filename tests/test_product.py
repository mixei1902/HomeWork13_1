import pytest

from src.product import Product, LawnGrass, Smartphone


@pytest.fixture
def product():
    return Product("fruit", "fresh fruits", 120, 10)


def test_product_initialization(product):
    """ тест инициализации конструктора """
    assert product.name == "fruit"
    assert product.description == "fresh fruits"
    assert product.price == 120
    assert product.quantity == 10


def test_product(product):
    """ тест на изменение цены """
    product = Product("fruit", "fresh fruits", 120.0, 10)
    assert str(product) == "fruit, 120.0 руб. Остаток: 10 шт."
    assert product.price == 120.0
    product.price = 200.0
    assert product.price == 200.0
    product.price = -1
    assert product.price == 200.0


def test_product_addition(product):
    product1 = Product("fruit", "fresh fruits", 100.0, 10)
    product2 = Product("fruit", "fresh fruits", 200.0, 20)
    assert product1 + product2 == 100.0 * 10 + 200.0 * 20


def test_smartphone():
    """ тестирование класса Smartphone"""
    smartphone = Smartphone("iPhone 13", "Смартфон от Apple", 1000, 5, "Высокая", '13', 64, "Черный")
    assert smartphone.name == "iPhone 13"
    assert smartphone.description == "Смартфон от Apple"
    assert smartphone.price == 1000
    assert smartphone.quantity == 5
    assert smartphone.performance == "Высокая"
    assert smartphone.model == '13'
    assert smartphone.memory == 64
    assert smartphone.color == "Черный"


def test_lawn_grass():
    """ тестирование класса LawnGrass """
    lawn_grass = LawnGrass("Газонная трава", "Трава для газона", 500, 20, "Россия", "7 дней", "Зеленый")
    assert lawn_grass.name == "Газонная трава"
    assert lawn_grass.description == "Трава для газона"
    assert lawn_grass.price == 500
    assert lawn_grass.quantity == 20
    assert lawn_grass.country == "Россия"
    assert lawn_grass.germination_period == "7 дней"
    assert lawn_grass.color == "Зеленый"


# new_smartphone = Smartphone.create_product("iPhone 13", "Смартфон от Apple", 100000, 10, "Высокая", "13", 128, "Черный")
# new_lawn_grass = LawnGrass.create_product("Газонная трава", "Трава для газона", 500, 50, "Россия", "7 дней", "Зеленый")

def test_create_product_smartphone():
    name = "iPhone 13"
    description = "Смартфон от Apple"
    price = 100000
    quantity = 10
    performance = "Высокая"
    model = "13"
    memory = 128
    color = "Черный"

    product = Smartphone.create_product(name, description, price, quantity, performance, model, memory, color)

    assert product.name == name
    assert product.description == description
    assert product.price == price
    assert product.quantity == quantity
    assert product.performance == performance
    assert product.model == model
    assert product.memory == memory
    assert product.color == color


def test_create_product_lawngrass():
    name = "Газонная трава"
    description = "Трава для газона"
    price = 500
    quantity = 50
    country = "Россия"
    germination_period = "7 дней"
    color = "Зеленый"

    product = LawnGrass.create_product(name, description, price, quantity, country, germination_period, color)

    assert product.name == name
    assert product.description == description
    assert product.price == price
    assert product.quantity == quantity
    assert product.country == country
    assert product.germination_period == germination_period
    assert product.color == color
