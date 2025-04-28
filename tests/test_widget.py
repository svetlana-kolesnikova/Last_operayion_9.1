import pytest

from src.widget import mask_account_card


@pytest.mark.parametrize(
    "example_count_number, example_masked_count_number",
    [
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
        ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
    ],
)
def test_mask_account_card_right(example_count_number: str, example_masked_count_number: str) -> None:
    """Тест с правильно введённым номером счёта"""
    assert mask_account_card(example_count_number) == example_masked_count_number


@pytest.mark.parametrize(
    "example_count_number, error_message",
    [
        ("Счет 73654108430135874", "Invalid type of number"),
        ("Счет 353830334744478s5560", "Invalid type of number"),
        ("Счет 736541084301358743055", "Invalid type of number"),
        ("Maestro 159683786870519", "Invalid type of number"),
        ("MasterCard 71583007347267j8", "Invalid type of number"),
        ("Visa Classic 6831982476737k65", "Invalid type of number"),
        ("Visa Platinum 8990922113665", "Invalid type of number"),
        ("Visa Gold 599941422kk8426353", "Invalid type of number"),
    ],
)
def test_mask_account_card_error_type(example_count_number: str, error_message: str) -> None:
    """тестирование вызова ошибки при передаче неверного количества символов"""
    with pytest.raises(ValueError) as e_info:
        mask_account_card(example_count_number)
    assert str(e_info.value) == error_message
