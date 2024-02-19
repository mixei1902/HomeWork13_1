import pytest

from main import Category, Product


@pytest.fixture
def category():
    return Category("Electronics", "Devices and gadgets", ["Laptop", "Phone"])


@pytest.fixture
def product():
    return Product("Laptop", "Portable computer", 1000.99, 10)


def test_category_initialization(category):
    assert category.name == "Electronics"
    assert category.description == "Devices and gadgets"
    assert category.products == ["Laptop", "Phone"]


def test_product_initialization(product):
    assert product.name == "Laptop"
    assert product.description == "Portable computer"
    assert product.price == 1000.99
    assert product.quantity == 10


def test_product_count(category):
    assert Category.total_unique_products == 2


def test_category_count(category):
    assert Category.total_categories == 1
