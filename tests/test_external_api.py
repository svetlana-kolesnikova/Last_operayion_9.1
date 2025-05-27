from typing import Any
from unittest.mock import Mock, patch

from src.external_api import transaction_summ


@patch("src.external_api.requests.get")
def test_transaction_summ_usd_success(mock_get):
    """Тест для функции конвертации валюты при успешном
    обращении к стороннему сервису. Валюта "USD" """

    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"result": 7500.0}
    mock_get.return_value = mock_response

    transactions = [{"operationAmount": {"amount": "100", "currency": {"code": "USD"}}}]

    result = transaction_summ(transactions, "RUB")
    assert result == [7500.0]


@patch("src.external_api.requests.get")
def test_transaction_summ_faild(mock_get):
    """Тест для функции конвертации валюты при отсутствии ответа от стороннего сервиса"""
    mock_response = Mock()
    mock_response.status_code = 500
    mock_get.return_value = mock_response
    mock_get.return_value = mock_response
    transactions = [{"operationAmount": {"amount": "100", "currency": {"code": "USD"}}}]

    transaction_summ(transactions, "RUB")
    assert f"Не успешный запрос, код ошибки: 500"


def test_transaction_summ_no_operationamount(
    no_operationamount: list[dict[Any, Any]], sample_currency_rub: str
) -> Any:
    """Тест для проверки наличия ключа "operationAmount" """
    for transact in no_operationamount:
        operation_amount = transact.get("operationAmount")
        if not operation_amount:
            continue
        assert transaction_summ(no_operationamount, sample_currency_rub)


def test_transaction_summ_rub(no_amount: list[dict[Any, Any]], sample_currency_rub: str) -> Any:
    """Тест для проверки наличия ключа "amount" """
    for transact in no_amount:
        operation_amount = transact.get("operationAmount")
        amount_str = operation_amount.get("amount")
        currency = operation_amount.get("currency")
        transact_code = currency.get("code") if currency else None
        if amount_str is None or transact_code is None:
            continue
        assert transaction_summ(no_amount, sample_currency_rub)


def test_transaction_summ_invalid_amount(amount_none: list[dict[Any, Any]], sample_currency_rub: str) -> Any:
    """Тест проверяет, что функция возвращает пустой список"""
    result = transaction_summ(amount_none, sample_currency_rub)
    assert result == []
