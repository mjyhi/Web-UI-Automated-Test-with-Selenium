"""认证业务流测试（注册/登录）。"""

import os
from datetime import datetime

from ui_tests.core.base_test import BaseTest
from ui_tests.po.pages.community_page import CommunityPage
from ui_tests.po.pages.login_page import LoginPage
from ui_tests.po.pages.register_page import RegisterPage
from ui_tests.utils.data_loader import load_csv_dicts, load_json


class TestAuthFlow(BaseTest):
    """注册与登录业务流测试。"""

    def test_register_and_login_success(self):
        """注册成功后退出并再次登录成功（JSON 数据驱动）。"""
        data_path = os.path.join(
            os.path.dirname(os.path.dirname(__file__)), "data", "users.json"
        )
        data = load_json(data_path)
        register_data = data.get("register", {})

        username_prefix = register_data.get("username_prefix", "ui_test_user")
        password = register_data.get("password", "Test@123456")
        confirm_password = register_data.get("confirm_password", password)

        unique_suffix = datetime.now().strftime("%Y%m%d%H%M%S")
        username = f"{username_prefix}_{unique_suffix}"

        # 注册
        register_page = RegisterPage(self.driver, self.base_url)
        register_page.open_register()
        register_page.register(username, password, confirm_password)

        community_page = CommunityPage(self.driver, self.base_url)
        community_page.wait_until_url_contains("/community")
        self.assertTrue(community_page.is_logout_visible())

        # 退出
        community_page.logout()

        # 再次登录
        login_page = LoginPage(self.driver, self.base_url)
        login_page.open_login()
        login_page.login(username, password)

        community_page.wait_until_url_contains("/community")
        self.assertTrue(community_page.is_logout_visible())

    def test_login_success_with_csv_data(self):
        """读取 CSV 数据进行登录验证（可选）。"""
        data_path = os.path.join(
            os.path.dirname(os.path.dirname(__file__)), "data", "login_users.csv"
        )
        users = load_csv_dicts(data_path)

        # 支持环境变量注入账号
        env_user = os.getenv("UI_LOGIN_USERNAME")
        env_password = os.getenv("UI_LOGIN_PASSWORD")
        if env_user and env_password:
            users.insert(0, {"username": env_user, "password": env_password, "enabled": "true"})

        # 过滤启用的账号
        valid_users = []
        for user in users:
            enabled = str(user.get("enabled", "true")).lower() == "true"
            username = (user.get("username") or "").strip()
            password = (user.get("password") or "").strip()
            if enabled and username and password and "CHANGE_ME" not in username:
                valid_users.append({"username": username, "password": password})

        if not valid_users:
            self.skipTest("未配置可用的登录账号（CSV 或环境变量）。")

        for user in valid_users:
            with self.subTest(user=user["username"]):
                login_page = LoginPage(self.driver, self.base_url)
                login_page.open_login()
                login_page.login(user["username"], user["password"])

                community_page = CommunityPage(self.driver, self.base_url)
                community_page.wait_until_url_contains("/community")
                self.assertTrue(community_page.is_logout_visible())

                # 退出，避免影响后续用例
                community_page.logout()
