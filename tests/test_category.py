import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def category():
    return Category("food", "meat", ["pork", "chicken"])


def test_category_initialization(category):
    assert category.name == "food"
    assert category.description == "meat"
    assert category.products == ["pork", "chicken"]


def test_category_count(category):
    assert Category.total_categories == 1


def test_product_count(category):
    assert Category.total_unique_products == 2

def test_category():
    product1 = Product("Товар 1", "Описание товара 1", 100.0, 10)
    product2 = Product("Товар 2", "Описание товара 2", 200.0, 20)
    category = Category("Категория 1", "Описание категории 1", [product1])
    assert str(category) == "Категория 1, количество продуктов: 1 шт."
    category.add_product(product2)
    assert str(category) == "Категория 1, количество продуктов: 2 шт."
