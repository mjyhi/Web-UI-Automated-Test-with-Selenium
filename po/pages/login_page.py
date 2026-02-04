"""Login page object."""

from selenium.webdriver.common.by import By

from ui_tests.core.base_page import BasePage


class LoginPage(BasePage):
    """Page Object for the login page."""

    # Form fields
    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    SUBMIT = (By.CSS_SELECTOR, "button[type='submit']")
    # Error message
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".text-red-500")
    # Navigation to register
    SIGN_UP_LINK = (By.LINK_TEXT, "Don't have an account? Sign up")

    def open_login(self):
        """Open login page."""
        self.open("/login")

    def login(self, username: str, password: str):
        """Perform login action."""
        self.type(self.USERNAME, username)
        self.type(self.PASSWORD, password)
        self.click(self.SUBMIT)

    def is_login_form_visible(self) -> bool:
        """Check login form fields are visible."""
        return self.is_visible(self.USERNAME) and self.is_visible(self.PASSWORD)

    def get_error_message(self) -> str:
        """Return error message text."""
        return self.get_text(self.ERROR_MESSAGE)
