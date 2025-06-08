import re
from collections import Counter
from config import CATEGORIES


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
    return dict(Counter(
        transaction["description"].strip()
        for transaction in transactions_list
        if (desc := str(transaction.get("description", "")).strip()) and desc.lower() != "nan" and desc in allowed_types
    ))


if __name__ == "__main__":

    transactions = [
  {
    "id": 441945886,
    "state": "PENDING",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
  },
  {
    "id": 41428829,
    "state": "CANCELED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {
      "amount": "8221.37",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "MasterCard 7158300734726758",
    "to": "Счет 35383033474447895560"
  },
  {
    "id": 939719570,
    "state": "PENDING",
    "date": "2018-06-30T02:08:58.425572",
    "operationAmount": {
      "amount": "9824.07",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "Счет 75106830613657916952",
    "to": "Счет 11776614605963066702"
  },
  {
    "id": 587085106,
    "state": "EXECUTED",
    "date": "2018-03-23T10:45:06.972075",
    "operationAmount": {
      "amount": "48223.05",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Открытие вклада",
    "to": "Счет 41421565395219882431"
  },
  {
    "id": 142264268,
    "state": "CANCELED",
    "date": "2019-04-04T23:20:05.206878",
    "operationAmount": {
      "amount": "79114.93",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод со счета на счет",
    "from": "Счет 19708645243227258542",
    "to": "Счет 75651667383060284188"
  },
  {
    "id": 873106923,
    "state": "EXECUTED",
    "date": "2019-03-23T01:09:46.296404",
    "operationAmount": {
      "amount": "43318.34",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод со счета на счет",
    "from": "Счет 44812258784861134719",
    "to": "Счет 74489636417521191160"
  }
    ]
    
    print(transactions_counter_by_type(transactions, CATEGORIES))
