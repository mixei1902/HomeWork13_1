import pytest

from src.category import Category


@pytest.fixture
def category():
    return Category("food", "meat", ["pork", "chiken"])


def test_category_initialization(category):
    assert category.name == "food"
    assert category.description == "meat"
    assert category.products == ["pork", "chiken"]


def test_category_count(category):
    assert Category.total_categories == 1


def test_product_count(category):
    assert Category.total_unique_products == 2
