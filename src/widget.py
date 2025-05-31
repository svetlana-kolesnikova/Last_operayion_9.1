def mask_account_card(account_card: str) -> str:
    """Функция обрабатывает информацию как о картах, так и о счетах"""
    split_account_card = account_card.split(" ")
    if "Счет" in account_card and len(account_card) != 25 or "Счет" in account_card and not account_card[5:].isdigit():
        raise ValueError("Invalid type of number")

    elif account_card[-17] == " " and not account_card[-16:].isdigit():
        raise ValueError("Invalid type of number")

    elif "Счет" in account_card and len(account_card) == 25:
        mask_account_number = split_account_card[-1].replace(split_account_card[-1][0:16], "**")
        split_account_card[-1] = mask_account_number
        account_number_masked = " ".join(split_account_card)

        return account_number_masked

    elif account_card[-17] != " " and not account_card[-16:].isdigit():
        raise ValueError("Invalid type of number")

    else:
        mask_number_card = (
            f"{split_account_card[-1][:4]} {split_account_card[-1][4:6]}** **** {split_account_card[-1][12:]}"
        )
    split_account_card[-1] = mask_number_card
    number_card_masked = " ".join(split_account_card)

    return number_card_masked


def get_date(date: str) -> str:
    """Функция возвращает время в формате "ДД.ММ.ГГГГ" """
    for date_part in date[:10].split("-"):
        if not date_part.isdigit():
            raise ValueError("Invalid type of date")

        elif date_part.isdigit():
            date_fixed = ".".join(list(reversed(date[:10].split("-"))))

    return date_fixed
