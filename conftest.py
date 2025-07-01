import pytest

from pages.login_page import Login_page
from pages.product_page import Product_page


@pytest.fixture
def login_page(page):
    return Login_page(page)


@pytest.fixture
def product_page(page):
    return Product_page(page)