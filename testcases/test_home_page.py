"""首页 UI 测试。"""

from ui_tests.core.base_test import BaseTest
from ui_tests.po.pages.home_page import HomePage


class TestHomePage(BaseTest):
    """验证首页关键元素。"""

    def test_home_hero_title(self):
        page = HomePage(self.driver, self.base_url)
        page.open_home()
        # 断言 Hero 标题
        self.assertEqual(page.get_hero_title(), "Teach Smarter with AI")

    def test_home_navigation_visible(self):
        page = HomePage(self.driver, self.base_url)
        page.open_home()
        # 断言导航可见
        self.assertTrue(page.is_nav_visible())
