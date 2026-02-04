"""Home page UI tests."""

from ui_tests.core.base_test import BaseTest
from ui_tests.po.pages.home_page import HomePage


class TestHomePage(BaseTest):
    """Verify key elements on home page."""

    def test_home_hero_title(self):
        page = HomePage(self.driver, self.base_url)
        page.open_home()
        # Assert hero title text
        self.assertEqual(page.get_hero_title(), "Teach Smarter with AI")

    def test_home_navigation_visible(self):
        page = HomePage(self.driver, self.base_url)
        page.open_home()
        # Assert nav links are visible
        self.assertTrue(page.is_nav_visible())
