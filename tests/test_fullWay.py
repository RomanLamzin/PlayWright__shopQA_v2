import pytest

standard_user = 'standard_user'
password_common = 'secret_sauce'
#
title_product = 'Products'
url_product_page = 'https://www.saucedemo.com/inventory.html'



def test_fullWay_standart(login_page, product_page):
    login_page.navigate()
    login_page.login(standard_user, password_common)

    product_page.assert_product_page(title_product, url_product_page)
