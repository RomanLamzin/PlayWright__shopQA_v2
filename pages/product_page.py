from playwright.sync_api import Page, expect


class Product_page():

    def __init__(self, page: Page):
        self.page = page
        self.product_title = page.locator("[data-test='title']")

    def assert_product_page(self, title, url):
        cur_url = self.page.url
        expect(self.product_title).to_have_text(title)
        assert url == cur_url
