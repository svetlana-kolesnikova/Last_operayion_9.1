import pytest

from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number() -> None:
    """тестирование при вхождении правильных данных"""
    assert get_mask_card_number("7000792289606361") == "7000 79** **** 6361"


def test_get_mask_card_number_less_than_16(digit_number_wrong: str) -> None:
    """тестирование вызова ошибки при передаче неверного количества символов"""
    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number(digit_number_wrong)
    assert str(exc_info.value) == "Invalid card number"


def test_get_mask_card_number_not_isdigit(digit_alpha_number_wrong: str) -> None:
    """тестирование вызова ошибки при передаче неверного типа данных"""
    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number(digit_alpha_number_wrong)
    assert str(exc_info.value) == "Invalid card number"


def test_get_mask_account_right() -> None:
    """тестирование при вхождении правильных данных"""
    assert get_mask_account("73654108430135874305") == "**4305"


def test_get_mask_account_less_than_20(digit_number_wrong: str) -> None:
    """тестирование вызова ошибки при передаче неверного количества символов"""
    with pytest.raises(ValueError) as exc_info:
        get_mask_account(digit_number_wrong)
    assert str(exc_info.value) == "Invalid account number"


def test_get_mask_account_not_isdigit(digit_alpha_number_wrong: str) -> None:
    """тестирование вызова ошибки при передаче неверного типа данных"""
    with pytest.raises(ValueError) as exc_info:
        get_mask_account(digit_alpha_number_wrong)
    assert str(exc_info.value) == "Invalid account number"
