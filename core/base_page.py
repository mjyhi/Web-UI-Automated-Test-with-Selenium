"""Base Page Object with common UI operations."""

from datetime import datetime
from typing import Optional, Tuple
from urllib.parse import urlparse

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from ui_tests.utils.exceptions import ElementNotFoundError
from ui_tests.utils.logger import get_logger


Locator = Tuple[str, str]


class BasePage:
    def __init__(self, driver: WebDriver, base_url: str, timeout: int = 10):
        self.driver = driver
        self.base_url = base_url.rstrip("/")
        # Explicit wait for stable element operations
        self.wait = WebDriverWait(driver, timeout)
        self.logger = get_logger(self.__class__.__name__, self._default_log_dir())

    @staticmethod
    def _default_log_dir() -> str:
        from pathlib import Path

        base_dir = Path(__file__).resolve().parents[1]
        return str(base_dir / "logs")

    def _build_url(self, path: str) -> str:
        """Join base_url with a path or accept full URL."""
        if not path:
            return self.base_url
        parsed = urlparse(path)
        if parsed.scheme and parsed.netloc:
            return path
        return f"{self.base_url}/{path.lstrip('/')}"

    def open(self, path: str = "") -> None:
        """Open a page by relative path or absolute URL."""
        url = self._build_url(path)
        self.logger.info("Opening URL: %s", url)
        self.driver.get(url)

    def find(self, locator: Locator):
        """Find element present in DOM."""
        try:
            return self.wait.until(EC.presence_of_element_located(locator))
        except Exception as exc:
            self.logger.error("Element not found: %s", locator)
            raise ElementNotFoundError(str(locator)) from exc

    def find_visible(self, locator: Locator):
        """Find element that is visible on the page."""
        try:
            return self.wait.until(EC.visibility_of_element_located(locator))
        except Exception as exc:
            self.logger.error("Visible element not found: %s", locator)
            raise ElementNotFoundError(str(locator)) from exc

    def find_all(self, locator: Locator):
        """Find all matching elements without explicit wait."""
        return self.driver.find_elements(*locator)

    def click(self, locator: Locator) -> None:
        """Click when element is clickable."""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def type(self, locator: Locator, text: str, clear: bool = True) -> None:
        """Type into input; clear by default."""
        element = self.find_visible(locator)
        if clear:
            element.clear()
        element.send_keys(text)

    def get_text(self, locator: Locator) -> str:
        """Get visible text from element."""
        return self.find_visible(locator).text

    def is_visible(self, locator: Locator) -> bool:
        """Return True if element is visible, else False."""
        try:
            self.find_visible(locator)
            return True
        except ElementNotFoundError:
            return False

    def save_screenshot(self, directory: str, name: Optional[str] = None) -> str:
        """Save a screenshot into the given directory."""
        from pathlib import Path

        Path(directory).mkdir(parents=True, exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        file_name = name or f"screenshot_{timestamp}.png"
        file_path = str(Path(directory) / file_name)
        self.driver.save_screenshot(file_path)
        self.logger.info("Saved screenshot: %s", file_path)
        return file_path
