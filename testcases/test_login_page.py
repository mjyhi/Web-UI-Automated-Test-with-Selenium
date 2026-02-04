"""Login page UI tests."""

from ui_tests.core.base_test import BaseTest
from ui_tests.po.pages.login_page import LoginPage


class TestLoginPage(BaseTest):
    """Verify login page elements."""

    def test_login_page_elements(self):
        page = LoginPage(self.driver, self.base_url)
        page.open_login()
        # Assert login form fields are visible
        self.assertTrue(page.is_login_form_visible())
