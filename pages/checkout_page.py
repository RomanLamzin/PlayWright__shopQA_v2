from time import sleep

from playwright.sync_api import Page, expect

from Base.base_class import Base


class Checkout_page(Base):

    def __init__(self, page: Page):
        self.page = page
        self.product_title = page.locator("[data-test='title']")
        self.firstNameInput = page.locator("[data-test='firstName']")
        self.lastNameInput = page.locator("[data-test='lastName']")
        self.postalCodeInput = page.locator("[data-test='postalCode']")
        self.continueBtn = page.locator("#continue")



    def fillUserInfoAndContinue(self):
        self.firstNameInput.fill('Romanio')
        self.lastNameInput.fill('Armanio')
        self.postalCodeInput.fill('443100')
        self.get_screenShot()
        sleep(1)
        self.continueBtn.click()





