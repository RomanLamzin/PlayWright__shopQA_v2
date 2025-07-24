from playwright.sync_api import expect

class Base():

    def assert_current_page(self, title, url):
        """Проверка  url и титульника страницы"""
        cur_url = self.page.url
        expect(self.product_title).to_have_text(title)
        assert url == cur_url
        print('Проверка  url и титульника страницы')