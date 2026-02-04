"""业务层：组合多个页面操作。"""

from ui_tests.po.pages.login_page import LoginPage
from ui_tests.po.pages.register_page import RegisterPage


class AuthBusiness:
    """认证相关业务流（登录/注册）。"""

    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url

    def login(self, username: str, password: str):
        """打开登录页并提交账号密码。"""
        page = LoginPage(self.driver, self.base_url)
        page.open_login()
        page.login(username, password)
        return page

    def register(self, username: str, password: str, confirm_password: str):
        """打开注册页并提交注册表单。"""
        page = RegisterPage(self.driver, self.base_url)
        page.open_register()
        page.register(username, password, confirm_password)
        return page
