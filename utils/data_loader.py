"""Simple test data loader utilities."""

import json
from typing import Any


def load_json(path: str) -> Any:
    """Load JSON data from a file."""
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)
