from playwright.sync_api import Page, expect

from Base.base_class import Base


class Complete_page(Base):

    def __init__(self, page: Page):
        self.page = page
        self.product_title = page.locator("[data-test='title']")

        self.image = page.locator("[data-test='pony-express']")
        self.approved_text = page.locator("[data-test='complete-header']")




    def check_order_confirm(self):
        expect(self.image).to_be_visible()
        assert self.approved_text.inner_text() == "Thank you for your order!"
        self.get_screenShot()
