import pytest

from src.product import Product


@pytest.fixture
def product():
    return Product("fruit", "fresh fruits", 120, 10)


def test_product_initialization(product):
    assert product.name == "fruit"
    assert product.description == "fresh fruits"
    assert product.price == 120
    assert product.quantity == 10

def test_product(product):
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


