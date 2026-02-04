"""测试基类（统一管理 WebDriver 生命周期）。"""

import os
import unittest
from datetime import datetime
from urllib.error import URLError
from urllib.request import Request, urlopen

from ui_tests.core.driver_factory import DriverFactory
from ui_tests.utils.config_loader import load_config
from ui_tests.utils.logger import get_logger


class BaseTest(unittest.TestCase):
    """所有 UI 用例的公共基类。"""
    driver = None
    config = None
    base_url = None
    logger = None

    @classmethod
    def setUpClass(cls):
        """初始化驱动与全局配置。"""
        cls.config = load_config()
        logs_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "logs")
        cls.logger = get_logger("UITest", logs_dir)

        # 可选：当目标服务不可用时跳过测试
        require_server = os.getenv("UI_REQUIRE_SERVER", "false").lower() in {
            "1",
            "true",
            "yes",
        }
        if not cls._is_server_available(cls.config.base_url):
            message = f"目标服务不可访问：{cls.config.base_url}"
            if require_server:
                raise RuntimeError(message)
            raise unittest.SkipTest(message)

        cls.driver = DriverFactory.create_driver(cls.config)
        cls.driver.implicitly_wait(cls.config.implicit_wait)
        cls.driver.set_page_load_timeout(cls.config.page_load)
        cls.driver.set_script_timeout(cls.config.script_timeout)
        cls.base_url = cls.config.base_url

    def tearDown(self):
        """失败时自动截图。"""
        if self._test_failed():
            self._capture_screenshot()

    @classmethod
    def tearDownClass(cls):
        """关闭驱动。"""
        if cls.driver:
            cls.driver.quit()

    def _test_failed(self) -> bool:
        """判断当前用例是否失败。"""
        outcome = getattr(self, "_outcome", None)
        if not outcome:
            return False

        errors = []
        failures = []

        if hasattr(outcome, "errors"):
            errors = outcome.errors
        result = getattr(outcome, "result", None)
        if result is not None:
            errors = errors or result.errors
            failures = result.failures

        return any(err for (_, err) in errors + failures)

    def _capture_screenshot(self) -> None:
        """保存失败截图。"""
        screenshots_dir = os.path.join(
            os.path.dirname(os.path.dirname(__file__)), "screenshots"
        )
        os.makedirs(screenshots_dir, exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{self.__class__.__name__}_{self._testMethodName}_{timestamp}.png"
        path = os.path.join(screenshots_dir, filename)
        try:
            self.driver.save_screenshot(path)
            self.logger.info("Saved failure screenshot: %s", path)
        except Exception as exc:
            self.logger.error("Failed to save screenshot: %s", exc)

    @staticmethod
    def _is_server_available(base_url: str) -> bool:
        """简单健康检查，判断目标服务是否可访问。"""
        try:
            request = Request(base_url, headers={"User-Agent": "Mozilla/5.0"})
            with urlopen(request, timeout=5) as response:
                return response.status < 500
        except (URLError, ValueError):
            return False
