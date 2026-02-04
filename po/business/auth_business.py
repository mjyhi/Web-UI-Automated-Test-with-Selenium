"""Business flows combining multiple page operations."""

from ui_tests.po.pages.login_page import LoginPage
from ui_tests.po.pages.register_page import RegisterPage


class AuthBusiness:
    """Auth related business flows (login/register)."""

    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url

    def login(self, username: str, password: str):
        """Open login page and submit credentials."""
        page = LoginPage(self.driver, self.base_url)
        page.open_login()
        page.login(username, password)
        return page

    def register(self, username: str, password: str, confirm_password: str):
        """Open register page and submit registration form."""
        page = RegisterPage(self.driver, self.base_url)
        page.open_register()
        page.register(username, password, confirm_password)
        return page
