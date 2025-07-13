from playwright.sync_api import Page, expect


class Cart_page():

    def __init__(self, page: Page):
        self.page = page
        self.product_title = page.locator("[data-test='title']")
        self.nameOfProductInCart = page.locator("[data-test='inventory-item-name']")
        self.priceOfProductInCart = page.locator("[data-test='inventory-item-price']")
        self.checkoutBtn = page.locator("#checkout")


    def assert_cart_page(self, title, url):
        """Проверка  url и титульника страницы cart"""
        cur_url = self.page.url
        expect(self.product_title).to_have_text(title)
        assert url == cur_url
        print(self.nameOfProductInCart.inner_text())
        print(self.priceOfProductInCart.inner_text())

    def checkProductNameAndPrice(self, p_price):
        """Проверка коррректности переноса  продукта по его имени и цене"""
        assert self.nameOfProductInCart.inner_text() == 'Sauce Labs Bike Light'

        self.cart_p = float(self.priceOfProductInCart.inner_text().replace('$',''))
        assert p_price == self.cart_p
        self.checkoutBtn.click()
