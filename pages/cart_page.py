from time import sleep

from playwright.sync_api import Page, expect

from Base.base_class import Base


class Cart_page(Base):

    def __init__(self, page: Page):
        self.page = page
        self.product_title = page.locator("[data-test='title']")
        self.nameOfProductInCart = page.locator("[data-test='inventory-item-name']")
        self.priceOfProductInCart = page.locator("[data-test='inventory-item-price']")
        self.checkoutBtn = page.locator("#checkout")




    def checkProductNameAndPrice(self, p_price):
        """Проверка коррректности переноса  продукта по его имени и цене"""
        assert self.nameOfProductInCart.inner_text() == 'Sauce Labs Bike Light'

        self.cart_p = float(self.priceOfProductInCart.inner_text().replace('$',''))
        assert p_price == self.cart_p
        self.get_screenShot()
        sleep(1)
        self.checkoutBtn.click()
