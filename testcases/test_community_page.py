"""Community page UI tests."""

from ui_tests.core.base_test import BaseTest
from ui_tests.po.pages.community_page import CommunityPage


class TestCommunityPage(BaseTest):
    """Verify community page elements."""

    def test_community_hero_title(self):
        page = CommunityPage(self.driver, self.base_url)
        page.open_community()
        # Assert hero title text
        self.assertEqual(page.get_hero_title(), "Teacher Community")

    def test_community_create_post_button_visible(self):
        page = CommunityPage(self.driver, self.base_url)
        page.open_community()
        # Assert create post button is visible
        self.assertTrue(page.has_create_post_button())
