import re
from collections import Counter


patterns = [
    re.compile(r'\bкарт\D*', re.IGNORECASE),
    re.compile(r'\bсчет\D*', re.IGNORECASE),
    re.compile(r'\bорганизац\D*', re.IGNORECASE),
    re.compile(r'\bвклад\D*', re.IGNORECASE)
]


def search_operation_by_description(transactions_list: list, description: str) -> list:
    """Функция для поиска в списке словарей операций по заданной строке "description" """
    filtered = []
    for transaction in transactions_list:
        transaction_desc = str(transaction.get("description", ""))  # Безопасное преобразование
        for pattern in patterns:
            if pattern.search(description) and pattern.search(transaction_desc):
                filtered.append(transaction)
                break  # Один матч достаточно
    return filtered


def transactions_counter_by_type(transactions_list: list, allowed_types: list) -> dict:
    """Функция для подсчёта количества банковских операций определенного типа"""
    types_list = []
    for transaction in transactions_list:
        state = str(transaction.get("state", "")).strip()
        if state.lower() == "nan" or not state:
            continue
        if state in allowed_types:
            types_list.append(state)
    return dict(Counter(types_list))
