"""Load runtime configuration from ini file."""

import configparser
import os
from dataclasses import dataclass
from typing import Optional, Tuple


@dataclass(frozen=True)
class Config:
    """Typed configuration object used across the framework."""
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
    """Parse common boolean string values."""
    return str(value).strip().lower() in {"1", "true", "yes", "y", "on"}


def _parse_window_size(value: str) -> Tuple[int, int]:
    """Parse 'width,height' string to tuple."""
    parts = [p.strip() for p in value.split(",") if p.strip()]
    if len(parts) != 2:
        return (1920, 1080)
    return (int(parts[0]), int(parts[1]))


def load_config(path: Optional[str] = None) -> Config:
    """Load config.ini; use defaults when keys are missing."""
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

    return Config(
        base_url=base_url,
        browser=browser,
        headless=headless,
        window_size=window_size,
        implicit_wait=implicit_wait,
        page_load=page_load,
        script_timeout=script_timeout,
    )
