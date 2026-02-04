"""WebDriver factory for different browsers."""

from selenium import webdriver

from ui_tests.utils.config_loader import Config


class DriverFactory:
    """Create WebDriver instances according to config."""

    @staticmethod
    def create_driver(config: Config):
        """Create a Selenium WebDriver based on the configured browser."""
        browser = config.browser.strip().lower()
        width, height = config.window_size

        if browser == "chrome":
            options = webdriver.ChromeOptions()
            if config.headless:
                options.add_argument("--headless=new")
            # Set window size for consistent screenshots/layouts
            options.add_argument(f"--window-size={width},{height}")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            driver = webdriver.Chrome(options=options)
        elif browser == "firefox":
            options = webdriver.FirefoxOptions()
            if config.headless:
                options.add_argument("-headless")
            driver = webdriver.Firefox(options=options)
            # Firefox uses a separate API for window size
            driver.set_window_size(width, height)
        elif browser == "edge":
            options = webdriver.EdgeOptions()
            if config.headless:
                options.add_argument("--headless=new")
            options.add_argument(f"--window-size={width},{height}")
            driver = webdriver.Edge(options=options)
        else:
            raise ValueError(f"Unsupported browser: {config.browser}")

        return driver
