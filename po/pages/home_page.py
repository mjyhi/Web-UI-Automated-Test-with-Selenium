"""Home page object."""

from selenium.webdriver.common.by import By

from ui_tests.core.base_page import BasePage


class HomePage(BasePage):
    """Page Object for the home page."""

    # Hero section title
    HERO_TITLE = (By.XPATH, "//h1[contains(text(), 'Teach Smarter with AI')]")
    # Navigation links
    NAV_HOME = (By.LINK_TEXT, "Home")
    NAV_ABOUT = (By.LINK_TEXT, "About")
    NAV_COURSES = (By.LINK_TEXT, "Courses")
    NAV_AI_TOOLS = (By.LINK_TEXT, "AI Tools")
    NAV_COMMUNITY = (By.LINK_TEXT, "Community")
    # Auth entry
    LOGIN_LINK = (By.LINK_TEXT, "Login")

    def open_home(self):
        """Open home page."""
        self.open("/")

    def get_hero_title(self) -> str:
        """Return hero title text."""
        return self.get_text(self.HERO_TITLE)

    def is_nav_visible(self) -> bool:
        """Check if top navigation is visible."""
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
        """Go to login page via header link."""
        self.click(self.LOGIN_LINK)
