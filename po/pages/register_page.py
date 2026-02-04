"""Register page object."""

from selenium.webdriver.common.by import By

from ui_tests.core.base_page import BasePage


class RegisterPage(BasePage):
    """Page Object for the register page."""

    # Form fields
    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    CONFIRM_PASSWORD = (By.ID, "confirm-password")
    SUBMIT = (By.CSS_SELECTOR, "button[type='submit']")
    # Error message
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".text-red-500")
    # Navigation to login
    SIGN_IN_LINK = (By.LINK_TEXT, "Already have an account? Sign in")

    def open_register(self):
        """Open register page."""
        self.open("/register")

    def register(self, username: str, password: str, confirm_password: str):
        """Perform registration action."""
        self.type(self.USERNAME, username)
        self.type(self.PASSWORD, password)
        self.type(self.CONFIRM_PASSWORD, confirm_password)
        self.click(self.SUBMIT)

    def is_register_form_visible(self) -> bool:
        """Check register form fields are visible."""
        return (
            self.is_visible(self.USERNAME)
            and self.is_visible(self.PASSWORD)
            and self.is_visible(self.CONFIRM_PASSWORD)
        )

    def get_error_message(self) -> str:
        """Return error message text."""
        return self.get_text(self.ERROR_MESSAGE)
