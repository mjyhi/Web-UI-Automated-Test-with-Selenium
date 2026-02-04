"""登录页 UI 测试。"""

from ui_tests.core.base_test import BaseTest
from ui_tests.po.pages.login_page import LoginPage


class TestLoginPage(BaseTest):
    """验证登录页元素。"""

    def test_login_page_elements(self):
        page = LoginPage(self.driver, self.base_url)
        page.open_login()
        # 断言登录表单可见
        self.assertTrue(page.is_login_form_visible())
