from playwright.sync_api import Page


class Login_page():

    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.locator('#user-name')
        self.password_input = page.locator('#password')
        self.login_button = page.locator('#login-button')
        self.error_message = page.locator('[data-test="error"]')


    # Actions

    def navigate(self):
        """Открыть страницу логина"""
        self.page.goto('https://www.saucedemo.com/')

    def login(self, username: str, password: str):
        """Выполняет вход с заданными учетными данными."""
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def get_error_msg(self):
        """Возвращает текст сообщения об ошибке."""

        print(self.error_message.inner_text())
        return self.error_message.inner_text()