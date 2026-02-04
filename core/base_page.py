"""页面基类（封装通用 UI 操作）。"""

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
        # 显式等待，保证元素操作稳定
        self.wait = WebDriverWait(driver, timeout)
        self.logger = get_logger(self.__class__.__name__, self._default_log_dir())

    @staticmethod
    def _default_log_dir() -> str:
        from pathlib import Path

        base_dir = Path(__file__).resolve().parents[1]
        return str(base_dir / "logs")

    def _build_url(self, path: str) -> str:
        """拼接 base_url 与相对路径，或直接使用绝对 URL。"""
        if not path:
            return self.base_url
        parsed = urlparse(path)
        if parsed.scheme and parsed.netloc:
            return path
        return f"{self.base_url}/{path.lstrip('/')}"

    def open(self, path: str = "") -> None:
        """打开页面（相对路径或绝对 URL）。"""
        url = self._build_url(path)
        self.logger.info("Opening URL: %s", url)
        self.driver.get(url)

    def find(self, locator: Locator):
        """查找 DOM 中存在的元素。"""
        try:
            return self.wait.until(EC.presence_of_element_located(locator))
        except Exception as exc:
            self.logger.error("Element not found: %s", locator)
            raise ElementNotFoundError(str(locator)) from exc

    def find_visible(self, locator: Locator):
        """查找页面可见元素。"""
        try:
            return self.wait.until(EC.visibility_of_element_located(locator))
        except Exception as exc:
            self.logger.error("Visible element not found: %s", locator)
            raise ElementNotFoundError(str(locator)) from exc

    def find_all(self, locator: Locator):
        """查找所有匹配元素（不等待）。"""
        return self.driver.find_elements(*locator)

    def click(self, locator: Locator) -> None:
        """点击可点击元素。"""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def type(self, locator: Locator, text: str, clear: bool = True) -> None:
        """输入文本（默认先清空）。"""
        element = self.find_visible(locator)
        if clear:
            element.clear()
        element.send_keys(text)

    def get_text(self, locator: Locator) -> str:
        """获取元素可见文本。"""
        return self.find_visible(locator).text

    def is_visible(self, locator: Locator) -> bool:
        """判断元素是否可见。"""
        try:
            self.find_visible(locator)
            return True
        except ElementNotFoundError:
            return False

    def wait_until_url_contains(self, text: str, timeout: int = 10) -> bool:
        """等待 URL 包含指定字符串。"""
        return WebDriverWait(self.driver, timeout).until(EC.url_contains(text))

    def get_current_url(self) -> str:
        """获取当前页面 URL。"""
        return self.driver.current_url

    def save_screenshot(self, directory: str, name: Optional[str] = None) -> str:
        """保存截图到指定目录。"""
        from pathlib import Path

        Path(directory).mkdir(parents=True, exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        file_name = name or f"screenshot_{timestamp}.png"
        file_path = str(Path(directory) / file_name)
        self.driver.save_screenshot(file_path)
        self.logger.info("Saved screenshot: %s", file_path)
        return file_path
