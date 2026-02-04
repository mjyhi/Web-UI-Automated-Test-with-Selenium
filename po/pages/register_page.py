"""注册页 Page Object。"""

from selenium.webdriver.common.by import By

from ui_tests.core.base_page import BasePage


class RegisterPage(BasePage):
    """注册页页面对象。"""

    # 表单字段
    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    CONFIRM_PASSWORD = (By.ID, "confirm-password")
    SUBMIT = (By.CSS_SELECTOR, "button[type='submit']")
    # 错误提示
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".text-red-500")
    # 跳转到登录页
    SIGN_IN_LINK = (By.LINK_TEXT, "Already have an account? Sign in")

    def open_register(self):
        """打开注册页。"""
        self.open("/register")

    def register(self, username: str, password: str, confirm_password: str):
        """执行注册操作。"""
        self.type(self.USERNAME, username)
        self.type(self.PASSWORD, password)
        self.type(self.CONFIRM_PASSWORD, confirm_password)
        self.click(self.SUBMIT)

    def is_register_form_visible(self) -> bool:
        """判断注册表单是否可见。"""
        return (
            self.is_visible(self.USERNAME)
            and self.is_visible(self.PASSWORD)
            and self.is_visible(self.CONFIRM_PASSWORD)
        )

    def get_error_message(self) -> str:
        """获取错误提示文本。"""
        return self.get_text(self.ERROR_MESSAGE)
