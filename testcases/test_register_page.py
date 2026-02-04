"""Register page UI tests."""

from ui_tests.core.base_test import BaseTest
from ui_tests.po.pages.register_page import RegisterPage


class TestRegisterPage(BaseTest):
    """Verify register page elements."""

    def test_register_page_elements(self):
        page = RegisterPage(self.driver, self.base_url)
        page.open_register()
        # Assert register form fields are visible
        self.assertTrue(page.is_register_form_visible())
