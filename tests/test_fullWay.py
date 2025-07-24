import pytest
import val_file as vf

"""Смок тест основоного БП (покупка товара)"""


def test_fullWay_standart(login_page, product_page, cart_page, checkout_page, overview_page, complete_page):
    login_page.navigate()
    login_page.login(vf.standard_user, vf.password_common)

    product_page.assert_current_page(vf.title_product, vf.url_product_page)
    product_page.addBikeLightToCart()
    product_page.getBikeLightPrice_value()

    product_price = product_page.getBikeLightPrice_value()
    print(f"Цена на странице продукта за ед. товара = {product_price}")

    cart_page.assert_current_page(vf.title_cart, vf.url_cart_page)
    cart_page.checkProductNameAndPrice(product_price)

    checkout_page.assert_current_page(vf.title_checkout, vf.url_checkout_page)
    checkout_page.fillUserInfoAndContinue()

    overview_page.assert_current_page(vf.title_overview, vf.url_overview_page)
    overview_page.checkAllProductItem(product_price, vf.p_name)

    complete_page.assert_current_page(vf.title_complete, vf.url_complete_page)
    complete_page.check_order_confirm()
