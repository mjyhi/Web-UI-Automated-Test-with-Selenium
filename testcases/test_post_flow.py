"""发帖业务流测试。"""

import os
from datetime import datetime

from ui_tests.core.base_test import BaseTest
from ui_tests.po.business.community_business import CommunityBusiness
from ui_tests.po.pages.community_page import CommunityPage
from ui_tests.po.pages.register_page import RegisterPage
from ui_tests.utils.data_loader import load_json


class TestPostFlow(BaseTest):
    """验证登录后发帖流程。"""

    def test_create_post_success(self):
        """注册后发布帖子（JSON 数据驱动）。"""
        base_dir = os.path.dirname(os.path.dirname(__file__))
        user_data = load_json(os.path.join(base_dir, "data", "users.json"))
        post_data = load_json(os.path.join(base_dir, "data", "posts.json"))

        register_data = user_data.get("register", {})
        post_info = post_data.get("post", {})

        username_prefix = register_data.get("username_prefix", "ui_test_user")
        password = register_data.get("password", "Test@123456")
        confirm_password = register_data.get("confirm_password", password)

        unique_suffix = datetime.now().strftime("%Y%m%d%H%M%S")
        username = f"{username_prefix}_{unique_suffix}"

        title_base = post_info.get("title", "UI 自动化发帖测试")
        content_base = post_info.get("content", "自动化测试发帖内容")
        title = f"{title_base}_{unique_suffix}"
        content = f"{content_base}（{unique_suffix}）"

        # 注册并登录
        register_page = RegisterPage(self.driver, self.base_url)
        register_page.open_register()
        register_page.register(username, password, confirm_password)

        community_page = CommunityPage(self.driver, self.base_url)
        community_page.wait_until_url_contains("/community")
        self.assertTrue(community_page.is_logout_visible())

        # 发帖
        community_business = CommunityBusiness(self.driver, self.base_url)
        community_business.create_post(title, content)

        community_page.wait_until_url_contains("/community")
        self.assertTrue(community_page.is_post_title_visible(title))
