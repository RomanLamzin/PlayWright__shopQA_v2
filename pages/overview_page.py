from playwright.sync_api import Page, expect


class Overview_page():

    def __init__(self, page: Page):
        self.page = page
        self.product_title = page.locator("[data-test='title']")

        self.itemName = page.locator("[data-test='inventory-item-name']")
        self.itemPrice = page.locator("[data-test='inventory-item-price']")
        self.itemTax = page.locator("[data-test='tax-label']")
        self.totalPrice = page.locator("[data-test='total-label']")

        self.finishBtn = page.locator("#finish")

    def assert_overview_page(self, title, url):
        """Проверка  url и титульника страницы Overview"""
        cur_url = self.page.url
        expect(self.product_title).to_have_text(title)
        assert url == cur_url

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

        self.finishBtn.click()

