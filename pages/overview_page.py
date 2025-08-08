from playwright.sync_api import Page, expect

from Base.base_class import Base


class Overview_page(Base):

    def __init__(self, page: Page):
        self.page = page
        self.product_title = page.locator("[data-test='title']")

        self.itemName = page.locator("[data-test='inventory-item-name']")
        self.itemPrice = page.locator("[data-test='inventory-item-price']")
        self.itemTax = page.locator("[data-test='tax-label']")
        self.totalPrice = page.locator("[data-test='total-label']")

        self.finishBtn = page.locator("#finish")



    def checkAllProductItem(self, p_price, p_name):

        """Проверка имени продукта, цены за единицу товара и общая цена с НДС => переход далее на сл страницу"""
        self.itemNameValue = self.itemName.inner_text()
        self.itemPriceValue = float(self.itemPrice.inner_text().replace('$', ''))
        self.itemTaxValue = self.itemTax.inner_text().split('$')[1:]
        self.totalPriceValue = self.totalPrice.inner_text().split('$')[1:]

        countPageTotalPrice = float(self.itemTaxValue[0]) + self.itemPriceValue
        countProductTotalPrice = float(self.itemTaxValue[0]) + p_price

        assert p_name == self.itemNameValue
        assert p_price == self.itemPriceValue
        assert countProductTotalPrice == countPageTotalPrice
        self.get_screenShot()

        self.finishBtn.click()

