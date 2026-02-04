"""社区页 UI 测试。"""

from ui_tests.core.base_test import BaseTest
from ui_tests.po.pages.community_page import CommunityPage


class TestCommunityPage(BaseTest):
    """验证社区页元素。"""

    def test_community_hero_title(self):
        page = CommunityPage(self.driver, self.base_url)
        page.open_community()
        # 断言 Hero 标题
        self.assertEqual(page.get_hero_title(), "Teacher Community")

    def test_community_create_post_button_visible(self):
        page = CommunityPage(self.driver, self.base_url)
        page.open_community()
        # 断言发帖按钮可见
        self.assertTrue(page.has_create_post_button())
