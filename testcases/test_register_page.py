"""注册页 UI 测试。"""

from ui_tests.core.base_test import BaseTest
from ui_tests.po.pages.register_page import RegisterPage


class TestRegisterPage(BaseTest):
    """验证注册页元素。"""

    def test_register_page_elements(self):
        page = RegisterPage(self.driver, self.base_url)
        page.open_register()
        # 断言注册表单可见
        self.assertTrue(page.is_register_form_visible())
