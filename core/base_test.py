"""Base unittest class with WebDriver lifecycle management."""

import os
import unittest
from datetime import datetime

from ui_tests.core.driver_factory import DriverFactory
from ui_tests.utils.config_loader import load_config
from ui_tests.utils.logger import get_logger


class BaseTest(unittest.TestCase):
    """Shared setup/teardown for all UI tests."""
    driver = None
    config = None
    base_url = None
    logger = None

    @classmethod
    def setUpClass(cls):
        """Initialize driver and global settings."""
        cls.config = load_config()
        logs_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "logs")
        cls.logger = get_logger("UITest", logs_dir)

        cls.driver = DriverFactory.create_driver(cls.config)
        cls.driver.implicitly_wait(cls.config.implicit_wait)
        cls.driver.set_page_load_timeout(cls.config.page_load)
        cls.driver.set_script_timeout(cls.config.script_timeout)
        cls.base_url = cls.config.base_url

    def tearDown(self):
        """Capture screenshot on failure."""
        if self._test_failed():
            self._capture_screenshot()

    @classmethod
    def tearDownClass(cls):
        """Quit driver when all tests complete."""
        if cls.driver:
            cls.driver.quit()

    def _test_failed(self) -> bool:
        """Check if current test has failed."""
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
        """Save failure screenshot into screenshots directory."""
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
