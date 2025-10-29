from typing import Any


def sorted_by_rub(transactions_: list[dict[Any, Any]]) -> list[dict[Any, Any]]:
    """Функция сортирует транзакции по значению "RUB" """
    filtered_by_rub = []
    for transact in transactions_:
        amount_str = transact.get("amount")
        currency_code = transact.get("currency_code")

        if amount_str is None or currency_code is None:
            continue

        if currency_code == "RUB":
            filtered_by_rub.append(transact)
    return filtered_by_rub
