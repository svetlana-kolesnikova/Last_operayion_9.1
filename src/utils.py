import json
from typing import Any, Dict, List, cast


def read_json(path: Any) -> list[dict[Any, Any]]:
    """Функция для чтения json-файла"""
    try:
        with open(path, encoding="utf-8") as f:
            return cast(List[Dict[Any, Any]], json.load(f))
    except (FileNotFoundError, json.JSONDecodeError):
        return []
