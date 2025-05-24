import json
import os
from typing import Any

import requests
from dotenv import load_dotenv

from config import PATH

path_to_json = PATH / "data" / "operations.json"

load_dotenv()

API_KEY = os.getenv('API_KEY')
payload: dict[Any, Any] = {}
headers = {"apikey": API_KEY}

currency_code = "RUB"

with open(path_to_json, encoding='utf-8') as file:
    """Чтение файла json"""
    transactions_ = json.load(file)


def transaction_summ(transactions: list[dict[Any, Any]], code: str) -> list[float] | str:
    """Функция конвертирует валюту и возвращает транзакции в рублях"""
    results_ = []
    for transact in transactions:
        operation_amount = transact.get("operationAmount")
        if not operation_amount:
            continue

        amount_str = operation_amount.get("amount")
        currency = operation_amount.get("currency")
        transact_code = currency.get("code") if currency else None

        if amount_str is None or transact_code is None:
            continue

        try:
            amount = float(amount_str)
        except (ValueError, TypeError):
            continue  # Пропускаем транзакцию с нечисловым значением

        if transact_code in ("USD", "EUR"):
            url = (
                f"https://api.apilayer.com/exchangerates_data/convert?"
                f"to={code}&from={transact_code}&amount={amount}"
            )
            response = requests.get(url, headers=headers, data=payload)
            if response.status_code == 200:
                result = response.json().get("result")
                if isinstance(result, (int, float)):
                    results_.append(result)
            else:
                return f"Не успешный запрос, код ошибки: {response.status_code}"
        elif transact_code == code:
            results_.append(amount)

    return results_


if __name__ == '__main__':
    print(transaction_summ(transactions_, currency_code))
