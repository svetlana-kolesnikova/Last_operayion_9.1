import json
import logging
from typing import Any, Dict, List, cast

from config import PATH


"""Логгирование модуля utils.py"""

logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("../logs/utils.log", "w")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)

path_to_json = PATH / "data" / "operations.json"


def read_json(path: Any) -> List[Dict[Any, Any]]:
    """Функция для чтения json-файла"""

    try:
        logger.debug("Выполняется чтение json-файла")
        with open(path, encoding="utf-8") as f:
            return cast(List[Dict[Any, Any]], json.load(f))
    except (FileNotFoundError, json.JSONDecodeError) as ex:
        logger.error(f"Произошла ошибка чтения json-файла {ex}")
        return []


result = read_json(path_to_json)
print(type(result))
