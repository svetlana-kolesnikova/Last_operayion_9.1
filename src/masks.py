import logging

"""Логгирование модуля masks.py"""

logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("../logs/masks.log", "w")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str:
    """Функция маскирует номер карты"""
    if not card_number.isdigit() or not len(card_number) == 16:
        logger.error("Произошла ошибка. Неверный номер карты")
        raise ValueError("Invalid card number")
    logger.debug("Выполняется маскировка номера карты")
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[12:]}"


def get_mask_account(account_number: str) -> str:
    """Функция маскирует номер счета"""
    if not account_number.isdigit() or not len(account_number) == 20:
        logger.error("Произошла ошибка. Неверный номер счёта")
        raise ValueError("Invalid account number")
    logger.debug("Выполняется маскировка номера счёта")
    return f"**{account_number[-4:]}"
