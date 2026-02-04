"""框架自定义异常。"""


class UIAutomationError(Exception):
    """UI 自动化框架基础异常。"""


class ElementNotFoundError(UIAutomationError):
    """元素未找到异常。"""
