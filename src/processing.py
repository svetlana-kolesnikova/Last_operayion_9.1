def filter_by_state(database: list, state: str = "EXECUTED") -> list:
    """Функция возвращает новый список словарей с данными банковских карт со значением state (по умолчанию)"""
    new_database = [item for item in database if item.get("state") == state]
    return new_database


def sort_by_date(date: list, ascending: bool = True) -> list:
    """Функция сортирует данные по дате и по убыванию (по умолчанию)"""
    data_sorted = sorted(date, key=lambda x: x.get("date", 0), reverse=ascending)
    return data_sorted
