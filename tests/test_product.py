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
    smartphone = Smartphone("Test Smartphone", "This is a test smartphone", 1000, 5, "High", "Model X", 64, "Black")
    assert smartphone.name == "Test Smartphone"
    assert smartphone.description == "This is a test smartphone"
    assert smartphone.price == 1000
    assert smartphone.quantity == 5
    assert smartphone.performance == "High"
    assert smartphone.model == "Model X"
    assert smartphone.memory == 64
    assert smartphone.color == "Black"


def test_lawn_grass():
    """ тестирование класса LawnGrass """
    lawn_grass = LawnGrass("Test Lawn Grass", "This is a test lawn grass", 500, 20, "USA", "7 days", "Green")
    assert lawn_grass.name == "Test Lawn Grass"
    assert lawn_grass.description == "This is a test lawn grass"
    assert lawn_grass.price == 500
    assert lawn_grass.quantity == 20
    assert lawn_grass.country == "USA"
    assert lawn_grass.germination_period == "7 days"
    assert lawn_grass.color == "Green"