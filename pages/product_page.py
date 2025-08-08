from playwright.sync_api import Page, expect

from Base.base_class import Base


class Product_page(Base):

    def __init__(self, page: Page):
        self.page = page
        self.product_title = page.locator("[data-test='title']")
        self.BikeLightBtn = page.locator("#add-to-cart-sauce-labs-bike-light")
        self.cartBtn = page.locator("#shopping_cart_container")
        self.BikeLightPrice_value = ''



    def addBikeLightToCart(self):
        """Добавляем товар в корзину и переходим в неё"""
        self.BikeLightBtn.click()

        """Cразу фиксируем стоимость товара"""
        self.BikeLightPrice = self.page.locator('//*[@id="remove-sauce-labs-bike-light"]/preceding-sibling::div[1]')
        self.BikeLightPrice_value = float(self.BikeLightPrice.inner_text().replace('$', ''))
        self.get_screenShot()
        self.cartBtn.click()

    def getBikeLightPrice_value(self):
        """для последующего использования цены товара за единицу продукции"""
        return self.BikeLightPrice_value
