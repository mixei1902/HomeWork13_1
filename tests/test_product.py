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
