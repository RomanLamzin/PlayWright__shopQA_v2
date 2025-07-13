import pytest

standard_user = 'standard_user'
password_common = 'secret_sauce'
# Product_page
title_product = 'Products'
url_product_page = 'https://www.saucedemo.com/inventory.html'
# Cart_page
title_cart = 'Your Cart'
url_cart_page = 'https://www.saucedemo.com/cart.html'
# Checkout_page
title_checkout = 'Checkout: Your Information'
url_checkout_page = 'https://www.saucedemo.com/checkout-step-one.html'
# Overview_page
title_overview= 'Checkout: Overview'
url_overview_page = 'https://www.saucedemo.com/checkout-step-two.html'
p_name = 'Sauce Labs Bike Light'



def test_fullWay_standart(login_page, product_page, cart_page, checkout_page, overview_page):
    login_page.navigate()
    login_page.login(standard_user, password_common)

    product_page.assert_product_page(title_product, url_product_page)
    product_page.addBikeLightToCart()
    product_page.getBikeLightPrice_value()

    product_price = product_page.getBikeLightPrice_value()
    print(f"Цена на странице продукта за ед. товара = {product_price}")

    cart_page.assert_cart_page(title_cart, url_cart_page)
    cart_page.checkProductNameAndPrice(product_price)

    checkout_page.assert_checkout_page(title_checkout, url_checkout_page)
    checkout_page.fillUserInfoAndContinue()

    overview_page.assert_overview_page(title_overview,url_overview_page)
    overview_page.checkAllProductItem(product_price, p_name)
