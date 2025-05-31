from typing import Any, Dict, List

import pandas as pd

from config import PATH

path_to_csv = PATH / "data" / "transactions.csv"
path_to_excel = PATH / "data" / "transactions_excel.xlsx"


def reader_csv(path: Any) -> List[Dict[Any, Any]]:
    """Функция для чтения файла csv. Возвращает список словарей с транзакциями"""
    try:
        reader = pd.read_csv(path)
        financial_operations_csv = reader.to_dict(orient="records")
        return financial_operations_csv
    except (FileNotFoundError, Exception):
        return []


def reader_excel(path: Any) -> List[Dict[Any, Any]]:
    """Функция для чтения файла excel. Возвращает список словарей с транзакциями"""
    try:
        reader = pd.read_excel(path)
        financial_operations_excel = reader.to_dict(orient="records")
        return financial_operations_excel
    except (FileNotFoundError, Exception):
        return []
