"""Custom exceptions for the UI automation framework."""


class UIAutomationError(Exception):
    """Base exception for UI automation framework."""


class ElementNotFoundError(UIAutomationError):
    """Raised when an expected element cannot be found."""
