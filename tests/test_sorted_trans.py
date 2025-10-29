from typing import Any

from src.sorted_trans import sorted_by_rub  # Замените на актуальный импорт


def test_sorted_by_rub_returns_only_rub(sample_transactions_rub_2: list[dict[Any, Any]]) -> Any:
    """Тестирование успешного возврата только рублевых транзакций"""
    result = sorted_by_rub(sample_transactions_rub_2)
    assert len(result) == 2
    assert all(tx["currency_code"] == "RUB" for tx in result)


def test_sorted_by_rub_empty_input() -> Any:
    """Тест возврата пустого списка"""
    assert sorted_by_rub([]) == []


def test_sorted_by_rub_all_non_rub() -> Any:
    """Тестирование функции при отсутствии рублевых транзакций"""
    transactions = [
        {"id": 1, "amount": 1000, "currency_code": "USD"},
        {"id": 2, "amount": 2000, "currency_code": "EUR"},
    ]
    result = sorted_by_rub(transactions)
    assert result == []


def test_sorted_by_rub_ignores_invalid_entries() -> Any:
    """Тестирование функции с отсутствием ключа "currency_code" """
    transactions = [
        {"id": 1, "currency_code": "RUB"},  # no amount
        {"id": 2, "amount": 1000},  # no currency_code
        {"id": 3, "amount": 1000, "currency_code": "RUB"},
    ]
    result = sorted_by_rub(transactions)
    assert len(result) == 1
    assert result[0]["id"] == 3
