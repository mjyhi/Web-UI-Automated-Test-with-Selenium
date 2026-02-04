"""测试数据加载工具（JSON/CSV）。"""

import csv
import json
from typing import Any, Dict, List


def load_json(path: str) -> Any:
    """读取 JSON 文件并返回数据。"""
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def load_csv_dicts(path: str) -> List[Dict[str, str]]:
    """读取 CSV 文件，返回字典列表（首行为表头）。"""
    with open(path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return [row for row in reader]
