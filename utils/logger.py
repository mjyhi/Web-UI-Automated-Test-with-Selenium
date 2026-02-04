"""Logging helpers for UI automation tests."""

import logging
import os
from datetime import datetime


_LOGGERS = {}


def get_logger(name: str, log_dir: str) -> logging.Logger:
    """Create or reuse a logger with file + console handlers."""
    if name in _LOGGERS:
        return _LOGGERS[name]

    os.makedirs(log_dir, exist_ok=True)
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    logger.propagate = False

    # Avoid duplicate handlers when calling multiple times.
    if not logger.handlers:
        timestamp = datetime.now().strftime("%Y%m%d")
        file_path = os.path.join(log_dir, f"ui_tests_{timestamp}.log")

        file_handler = logging.FileHandler(file_path, encoding="utf-8")
        file_handler.setLevel(logging.INFO)

        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)

        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(name)s - %(message)s"
        )
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    _LOGGERS[name] = logger
    return logger
