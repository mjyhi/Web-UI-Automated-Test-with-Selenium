"""Community page object."""

from selenium.webdriver.common.by import By

from ui_tests.core.base_page import BasePage


class CommunityPage(BasePage):
    """Page Object for the community page."""

    HERO_TITLE = (By.XPATH, "//h1[contains(text(), 'Teacher Community')]")
    CREATE_POST_BUTTON = (By.XPATH, "//button[contains(., 'Create Post')]")

    def open_community(self):
        """Open community page."""
        self.open("/community")

    def get_hero_title(self) -> str:
        """Return hero title text."""
        return self.get_text(self.HERO_TITLE)

    def has_create_post_button(self) -> bool:
        """Check if 'Create Post' button is visible."""
        return self.is_visible(self.CREATE_POST_BUTTON)
