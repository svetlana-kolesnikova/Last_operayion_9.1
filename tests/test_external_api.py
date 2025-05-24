from typing import Any
from unittest.mock import Mock
import pytest
import requests

from src.external_api import transaction_summ


def test_transaction_summ_usd_success(sample_transactions: list[dict[Any, Any]], sample_currency_rub: str) -> Any:
	"""Тест для функции конвертации валюты при успешном обращении к стороннему сервису. Валюта "USD" """
	mock_transaction_summ: Mock = Mock(return_value=[500.00])
	mock_status_code: Mock = Mock(return_value=200)
	for transact in sample_transactions:
		operation_amount = transact.get("operationAmount")
		currency = operation_amount.get("currency")
		transact_code = currency.get("code") if currency else None

		if transact_code in ("USD", "EUR"):
			requests.get = mock_transaction_summ
			response = mock_transaction_summ
			if response.status_code == mock_status_code:
				assert transaction_summ(sample_transactions, sample_currency_rub) == [500.00]
				mock_transaction_summ.assert_called_with(sample_transactions, sample_currency_rub)


def test_transaction_summ_no_operationamount(no_operationamount: list[dict[Any, Any]], sample_currency_rub: str) -> Any:
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


def test_transaction_summ_(amount_none, sample_currency_rub):
	for transact in amount_none:
		if transact["operationAmount"]["amount"] is None:
			with pytest.raises(ValueError, TypeError):
				transaction_summ(amount_none, sample_currency_rub)

