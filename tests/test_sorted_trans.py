from src.sorted_trans import sorted_by_rub  # Замените на актуальный импорт


def test_sorted_by_rub_returns_only_rub(sample_transactions_rub_2):
    result = sorted_by_rub(sample_transactions_rub_2)
    assert len(result) == 2
    assert all(tx["currency_code"] == "RUB" for tx in result)

def test_sorted_by_rub_empty_input():
    assert sorted_by_rub([]) == []

def test_sorted_by_rub_all_non_rub():
    transactions = [
        {"id": 1, "amount": 1000, "currency_code": "USD"},
        {"id": 2, "amount": 2000, "currency_code": "EUR"},
    ]
    result = sorted_by_rub(transactions)
    assert result == []

def test_sorted_by_rub_ignores_invalid_entries():
    transactions = [
        {"id": 1, "currency_code": "RUB"},  # no amount
        {"id": 2, "amount": 1000},          # no currency_code
        {"id": 3, "amount": 1000, "currency_code": "RUB"},
    ]
    result = sorted_by_rub(transactions)
    assert len(result) == 1
    assert result[0]["id"] == 3