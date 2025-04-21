def filter_by_state(database: list, state: str = "EXECUTED") -> list:
    """Функция возвращает новй список словарей с указанным значением state"""
    new_database = []
    for i in database:
        for key in i.keys():
            if i[key] == state:
                new_database.append(i)

    return new_database

