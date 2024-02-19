import pytest

from main import Category, Product


@pytest.fixture
def category():
    return Category("food", "meat", ["pork", "chiken"])


@pytest.fixture
def product():
    return Product("fruit", "fresh fruits", 120, 10)


def test_category_initialization(category):
    assert category.name == "food"
    assert category.description == "meat"
    assert category.products == ["pork", "chiken"]


def test_product_initialization(product):
    assert product.name == "fruit"
    assert product.description == "fresh fruits"
    assert product.price == 120
    assert product.quantity == 10


def test_product_count(category):
    assert Category.total_unique_products == 2


def test_category_count(category):
    assert Category.total_categories == 1
