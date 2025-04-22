def mask_account_card(account_card: str) -> str:
    """Функция обрабатывает информацию как о картах, так и о счетах"""
    split_account_card = account_card.split(" ")
    if "Счет" in account_card:
        mask_account_number = split_account_card[-1].replace(split_account_card[-1][0:16], "**")
        split_account_card[-1] = mask_account_number
        account_number_masked = " ".join(split_account_card)

        return account_number_masked

    else:
        mask_number_card = (
            f"{split_account_card[-1][:4]} {split_account_card[-1][4:6]}** ****{split_account_card[-1][12:]}"
        )
    split_account_card[-1] = mask_number_card
    number_card_masked = " ".join(split_account_card)

    return number_card_masked


def get_date(date: str) -> str:
    """Функция возвращает время в формате "ДД.ММ.ГГГГ" """
    date_fixed = ".".join(list(reversed(date[:10].split("-"))))

    return date_fixed
