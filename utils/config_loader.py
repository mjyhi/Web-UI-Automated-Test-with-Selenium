"""读取运行配置（支持环境变量覆盖）。"""

import configparser
import os
from dataclasses import dataclass
from typing import Optional, Tuple


@dataclass(frozen=True)
class Config:
    """框架统一使用的配置对象。"""
    base_url: str
    browser: str
    headless: bool
    window_size: Tuple[int, int]
    implicit_wait: int
    page_load: int
    script_timeout: int


_DEF_CONFIG_PATH = os.path.join(
    os.path.dirname(os.path.dirname(__file__)), "config", "config.ini"
)


def _parse_bool(value: str) -> bool:
    """解析常见的布尔字符串。"""
    return str(value).strip().lower() in {"1", "true", "yes", "y", "on"}


def _parse_window_size(value: str) -> Tuple[int, int]:
    """解析 'width,height' 字符串为元组。"""
    parts = [p.strip() for p in value.split(",") if p.strip()]
    if len(parts) != 2:
        return (1920, 1080)
    return (int(parts[0]), int(parts[1]))


def load_config(path: Optional[str] = None) -> Config:
    """读取 config.ini，并支持环境变量覆盖。"""
    config_path = path or _DEF_CONFIG_PATH
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Config file not found: {config_path}")

    parser = configparser.ConfigParser()
    parser.read(config_path, encoding="utf-8")

    base_url = parser.get("server", "base_url", fallback="http://localhost:3000")
    browser = parser.get("browser", "name", fallback="chrome")
    headless = _parse_bool(parser.get("browser", "headless", fallback="true"))
    window_size = _parse_window_size(
        parser.get("browser", "window_size", fallback="1920,1080")
    )

    implicit_wait = parser.getint("timeouts", "implicit_wait", fallback=5)
    page_load = parser.getint("timeouts", "page_load", fallback=30)
    script_timeout = parser.getint("timeouts", "script_timeout", fallback=30)

    # 环境变量覆盖（用于 CI/不同环境）
    env_base_url = os.getenv("UI_BASE_URL")
    env_browser = os.getenv("UI_BROWSER")
    env_headless = os.getenv("UI_HEADLESS")
    env_window = os.getenv("UI_WINDOW_SIZE")
    env_implicit = os.getenv("UI_IMPLICIT_WAIT")
    env_page_load = os.getenv("UI_PAGE_LOAD")
    env_script = os.getenv("UI_SCRIPT_TIMEOUT")

    if env_base_url:
        base_url = env_base_url
    if env_browser:
        browser = env_browser
    if env_headless is not None:
        headless = _parse_bool(env_headless)
    if env_window:
        window_size = _parse_window_size(env_window)
    if env_implicit:
        implicit_wait = int(env_implicit)
    if env_page_load:
        page_load = int(env_page_load)
    if env_script:
        script_timeout = int(env_script)

    return Config(
        base_url=base_url,
        browser=browser,
        headless=headless,
        window_size=window_size,
        implicit_wait=implicit_wait,
        page_load=page_load,
        script_timeout=script_timeout,
    )
