"""日志工具（文件 + 控制台输出）。"""

import logging
import os
from datetime import datetime


_LOGGERS = {}


def get_logger(name: str, log_dir: str) -> logging.Logger:
    """创建或复用日志器（文件 + 控制台）。"""
    if name in _LOGGERS:
        return _LOGGERS[name]

    os.makedirs(log_dir, exist_ok=True)
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    logger.propagate = False

    # 避免重复添加 handler
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
