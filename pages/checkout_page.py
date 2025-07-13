
from playwright.sync_api import Page, expect


class Checkout_page():

    def __init__(self, page: Page):
        self.page = page
        self.product_title = page.locator("[data-test='title']")
        self.firstNameInput = page.locator("[data-test='firstName']")
        self.lastNameInput = page.locator("[data-test='lastName']")
        self.postalCodeInput = page.locator("[data-test='postalCode']")
        self.continueBtn = page.locator("#continue")


    def assert_checkout_page(self, title, url):
        """Проверка  url и титульника страницы Checkout"""
        cur_url = self.page.url
        expect(self.product_title).to_have_text(title)
        assert url == cur_url


    def fillUserInfoAndContinue(self):
        self.firstNameInput.fill('Romanio')
        self.lastNameInput.fill('Armanio')
        self.postalCodeInput.fill('443100')
        self.continueBtn.click()




