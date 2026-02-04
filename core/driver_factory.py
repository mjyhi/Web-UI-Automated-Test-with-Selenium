"""WebDriver 工厂（支持不同浏览器）。"""

from selenium import webdriver

from ui_tests.utils.config_loader import Config


class DriverFactory:
    """根据配置创建 WebDriver 实例。"""

    @staticmethod
    def create_driver(config: Config):
        """根据配置创建 Selenium WebDriver。"""
        browser = config.browser.strip().lower()
        width, height = config.window_size

        if browser == "chrome":
            options = webdriver.ChromeOptions()
            if config.headless:
                options.add_argument("--headless=new")
            # 设置窗口大小，保证布局与截图一致
            options.add_argument(f"--window-size={width},{height}")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            driver = webdriver.Chrome(options=options)
        elif browser == "firefox":
            options = webdriver.FirefoxOptions()
            if config.headless:
                options.add_argument("-headless")
            driver = webdriver.Firefox(options=options)
            # Firefox 使用单独的窗口尺寸 API
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
