"""发帖页 Page Object。"""

from selenium.webdriver.common.by import By

from ui_tests.core.base_page import BasePage


class NewPostPage(BasePage):
    """新建帖子页面对象。"""

    TITLE_INPUT = (By.ID, "title")
    CONTENT_TEXTAREA = (By.ID, "content")
    SUBMIT_BUTTON = (By.XPATH, "//button[contains(., 'Publish Post')]")
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".text-red-700")

    def open_new_post(self):
        """打开新建帖子页面。"""
        self.open("/community/new")

    def create_post(self, title: str, content: str):
        """填写并提交帖子。"""
        self.type(self.TITLE_INPUT, title)
        self.type(self.CONTENT_TEXTAREA, content)
        self.click(self.SUBMIT_BUTTON)

    def get_error_message(self) -> str:
        """获取错误提示文本。"""
        return self.get_text(self.ERROR_MESSAGE)
