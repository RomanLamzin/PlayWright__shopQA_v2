import pytest

from pages.checkout_page import Checkout_page
from pages.login_page import Login_page
from pages.overview_page import Overview_page
from pages.product_page import Product_page
from pages.cart_page import Cart_page


@pytest.fixture
def login_page(page):
    return Login_page(page)


@pytest.fixture
def product_page(page):
    return Product_page(page)

@pytest.fixture
def cart_page(page):
    return Cart_page(page)

@pytest.fixture
def checkout_page(page):
    return Checkout_page(page)

@pytest.fixture
def overview_page(page):
    return Overview_page(page)