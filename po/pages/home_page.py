"""首页 Page Object。"""

from selenium.webdriver.common.by import By

from ui_tests.core.base_page import BasePage


class HomePage(BasePage):
    """首页页面对象。"""

    # Hero 标题
    HERO_TITLE = (By.XPATH, "//h1[contains(text(), 'Teach Smarter with AI')]")
    # 导航链接
    NAV_HOME = (By.LINK_TEXT, "Home")
    NAV_ABOUT = (By.LINK_TEXT, "About")
    NAV_COURSES = (By.LINK_TEXT, "Courses")
    NAV_AI_TOOLS = (By.LINK_TEXT, "AI Tools")
    NAV_COMMUNITY = (By.LINK_TEXT, "Community")
    # 登录入口
    LOGIN_LINK = (By.LINK_TEXT, "Login")
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(., 'Logout')]")

    def open_home(self):
        """打开首页。"""
        self.open("/")

    def get_hero_title(self) -> str:
        """返回 Hero 标题文本。"""
        return self.get_text(self.HERO_TITLE)

    def is_nav_visible(self) -> bool:
        """判断顶部导航是否可见。"""
        return all(
            [
                self.is_visible(self.NAV_HOME),
                self.is_visible(self.NAV_ABOUT),
                self.is_visible(self.NAV_COURSES),
                self.is_visible(self.NAV_AI_TOOLS),
                self.is_visible(self.NAV_COMMUNITY),
            ]
        )

    def go_to_login(self):
        """点击登录入口。"""
        self.click(self.LOGIN_LINK)

    def is_logout_visible(self) -> bool:
        """判断是否已登录（Logout 按钮可见）。"""
        return self.is_visible(self.LOGOUT_BUTTON)

    def logout(self):
        """点击退出登录。"""
        self.click(self.LOGOUT_BUTTON)
