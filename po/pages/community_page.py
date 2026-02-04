"""社区页 Page Object。"""

from selenium.webdriver.common.by import By

from ui_tests.core.base_page import BasePage


class CommunityPage(BasePage):
    """社区页页面对象。"""

    HERO_TITLE = (By.XPATH, "//h1[contains(text(), 'Teacher Community')]")
    CREATE_POST_BUTTON = (By.XPATH, "//button[contains(., 'Create Post')]")
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(., 'Logout')]")
    POST_TITLES = (By.CSS_SELECTOR, "h3")

    def open_community(self):
        """打开社区页。"""
        self.open("/community")

    def get_hero_title(self) -> str:
        """获取 Hero 标题文本。"""
        return self.get_text(self.HERO_TITLE)

    def has_create_post_button(self) -> bool:
        """判断“Create Post”按钮是否可见。"""
        return self.is_visible(self.CREATE_POST_BUTTON)

    def is_logout_visible(self) -> bool:
        """判断是否已登录（Logout 按钮可见）。"""
        return self.is_visible(self.LOGOUT_BUTTON)

    def logout(self):
        """点击退出登录。"""
        self.click(self.LOGOUT_BUTTON)

    def is_post_title_visible(self, title: str) -> bool:
        """判断指定标题是否出现在帖子列表中。"""
        elements = self.find_all(self.POST_TITLES)
        return any(title.strip() == (el.text or "").strip() for el in elements)
