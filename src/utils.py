from typing import Any, cast, List, Dict
import json
from config import PATH

path_to_json = PATH /"data" / "operations.json"

def read_json(path: Any) -> List[Dict[Any, Any]]:
    """Функция для чтения json-файла"""
    try:
        with open(path, encoding="utf-8") as f:
            return cast(List[Dict[Any, Any]], json.load(f))
    except (FileNotFoundError, json.JSONDecodeError):
        return []

result = read_json(path_to_json)
print(type(result))
