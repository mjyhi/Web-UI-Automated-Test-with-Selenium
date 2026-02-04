"""登录页 Page Object。"""

from selenium.webdriver.common.by import By

from ui_tests.core.base_page import BasePage


class LoginPage(BasePage):
    """登录页页面对象。"""

    # 表单字段
    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    SUBMIT = (By.CSS_SELECTOR, "button[type='submit']")
    # 错误提示
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".text-red-500")
    # 跳转到注册页
    SIGN_UP_LINK = (By.LINK_TEXT, "Don't have an account? Sign up")

    def open_login(self):
        """打开登录页。"""
        self.open("/login")

    def login(self, username: str, password: str):
        """执行登录操作。"""
        self.type(self.USERNAME, username)
        self.type(self.PASSWORD, password)
        self.click(self.SUBMIT)

    def is_login_form_visible(self) -> bool:
        """判断登录表单是否可见。"""
        return self.is_visible(self.USERNAME) and self.is_visible(self.PASSWORD)

    def get_error_message(self) -> str:
        """获取错误提示文本。"""
        return self.get_text(self.ERROR_MESSAGE)
