from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_card_number_generator():
    """Тестирование функции с разным количеством десятков"""
    generator = card_number_generator(9, 12)
    assert next(generator) == "0000 0000 0000 0009"
    assert next(generator) == "0000 0000 0000 0010"
    assert next(generator) == "0000 0000 0000 0011"


def test_transaction_descriptions(sample_transactions: list) -> str:
    """Тестирование функции-генератора для вывода описания транзакций"""
    test_description = transaction_descriptions(sample_transactions)
    assert next(test_description) == "Перевод организации"
    assert next(test_description) == "Перевод со счета на счет"
    assert next(test_description) == "Перевод со счета на счет"


def test_filter_by_currency_success(sample_transactions: list, sample_currency_usd: str) -> dict:
    """Тест для функции, выводящей транзакции с заданной валютой"""

    usd_transactions = filter_by_currency(sample_transactions, sample_currency_usd)
    assert (next(usd_transactions)) == {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }
    assert (next(usd_transactions)) == {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    }
