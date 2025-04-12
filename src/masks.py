def get_mask_card_number(card_number: str) -> str:
    """Функция маскирует номер карты"""
    if not card_number.isdigit() or not len(card_number) == 16:
        raise ValueError("Invalid card number")

    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[12:]}"


def get_mask_account(account_number: str) -> str:
    """Функция маскирует номер счета"""
    if not account_number.isdigit() or not len(account_number) == 20:
        raise ValueError("Invalid account number")

    return f"**{account_number[-4:]}"
