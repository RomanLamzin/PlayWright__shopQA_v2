from playwright.sync_api import Page, expect


class Product_page():

    def __init__(self, page: Page):
        self.page = page
        self.product_title = page.locator("[data-test='title']")
        self.BikeLightBtn = page.locator("#add-to-cart-sauce-labs-bike-light")
        self.cartBtn = page.locator("#shopping_cart_container")
        self.BikeLightPrice_value = ''

    def assert_product_page(self, title, url):
        """Проверка  url и титульника страницы product"""
        cur_url = self.page.url
        expect(self.product_title).to_have_text(title)
        assert url == cur_url

    def addBikeLightToCart(self):
        """Добавляем товар в корзину и переходим в неё"""
        self.BikeLightBtn.click()

        """Cразу фиксируем стоимость товара"""
        self.BikeLightPrice = self.page.locator('//*[@id="remove-sauce-labs-bike-light"]/preceding-sibling::div[1]')
        self.BikeLightPrice_value = float(self.BikeLightPrice.inner_text().replace('$', ''))
        self.cartBtn.click()

    def getBikeLightPrice_value(self):
        """для последующего использования цены товара за единицу продукции"""
        return self.BikeLightPrice_value
