def filter_by_state(database: list, state: str = "EXECUTED") -> list:
    """Функция возвращает новй список словарей с указанным значением state"""
    new_database = []
    for i in database:
        for key in i.keys():
            if i[key] == state:
                new_database.append(i)

    return new_database


def sort_by_date(date: list, reverse_: bool = True) -> list:
    """Функция сортирует данные по дате и по убыванию (поумолчанию)"""
    data_sorted = sorted(date, key=lambda x: x.get("date", 0), reverse=reverse_)
    return data_sorted
