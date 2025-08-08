import datetime

from playwright.sync_api import Page, expect


class Base():

    def __init__(self, page: Page):
        self.page = page

    """ Метод проверки URL текущей страницы"""

    def assert_current_page(self, title, url):
        """Проверка  url и титульника страницы"""
        cur_url = self.page.url
        expect(self.product_title).to_have_text(title)
        assert url == cur_url
        print('Проверка  url и титульника страницы')

    """Метод Скриншота"""

    def get_screenShot(self):
        now_date = datetime.datetime.utcnow().strftime("%Y,%Ym,%d,%H,%M,%S")
        new_screen = f'screenShot {now_date} .jpeg'
        self.page.screenshot(path=f"screen\\{new_screen}", full_page=True)
