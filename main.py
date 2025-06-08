from typing import Any

import pandas as pd

from config import PATH_TO_CSV, PATH_TO_EXCEL, PATH_TO_JSON, TYPE_LIST
from src.csv_excel_reader import reader_csv, reader_excel
from src.filter_transactions import search_operation_by_description
from src.processing import filter_by_state, sort_by_date
from src.sorted_trans import sorted_by_rub
from src.utils import read_json
from src.widget import get_date, mask_account_card


def greeting() -> str:
    """Функция приветствия"""
    return """Привет! Добро пожаловать в программу работы
с банковскими транзакциями.
Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла
"""


print(greeting())

user_input_1 = int(input())

if user_input_1 not in [1, 2, 3]:
    print("Не корректный ввод. Попробуйте ещё раз")
else:

    def choose_using_file(user_input: int) -> Any:
        """Функция для выбора файла для чтения данных"""
        if user_input == 1:
            print("Для обработки выбран JSON-файл.")
            used_file_json = read_json(PATH_TO_JSON)
            return used_file_json
        elif user_input == 2:
            print("Для обработки выбран CSV-файл.")
            used_file_csv = reader_csv(PATH_TO_CSV)
            return used_file_csv
        elif user_input == 3:
            print("Для обработки выбран XLSX-файл.")
            used_file_excel = reader_excel(PATH_TO_EXCEL)
            return used_file_excel

    selected_file = choose_using_file(user_input_1)

    print("\nВведите статус, по которому необходимо выполнить фильтрацию.")
    print("Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n")

    while True:
        user_input_2 = input()

        if user_input_2.strip().upper() in TYPE_LIST:
            filtered_file = filter_by_state(selected_file, user_input_2)
            break  # выход из цикла при успешном вводе
        else:
            print(f"Статус операции '{user_input_2}' недоступен. Попробуйте снова.\n")

    """Программа предлагает отсортировать операции по дате"""

    print("\nОтсортировать операции по дате? Да/Нет\n")

    sorted_filtered_file = filtered_file
    while True:
        user_input_3 = input().strip().lower()
        if "да" in user_input_3 or "нет" in user_input_3:

            """Программа сортирует по дате"""

            if "да" in user_input_3:
                print("\nОтсортировать по возрастанию или по убыванию?\n")
                user_input_4 = input().lower()

                reverse_ = False if "возраст" in user_input_4 else True

                def date_sorted_file(filtered_file_: list[dict[Any, Any]]) -> Any:
                    sorted_ = sort_by_date(filtered_file_, reverse_)
                    return sorted_

                sorted_filtered_file = date_sorted_file(filtered_file)
            break  # выход из цикла при успешном вводе

        else:
            print("Введите Да/Нет\n")

    print("\nВыводить только рублевые транзакции? Да/Нет\n")
    sorted_by_currency = sorted_filtered_file
    while True:
        user_input_5 = input().strip().lower()
        if "да" in user_input_5 or "нет" in user_input_5:
            """Программа переводит валюту в рубли и рублевые транзакции"""
            if "да" in user_input_5:
                sorted_by_currency = sorted_by_rub(sorted_by_currency)
            break  # выход из цикла при успешном вводе
        else:
            print("Введите Да/Нет\n")

    print("\nОтфильтровать список транзакций по определенному слову в описании? Да/Нет\n")
    user_input_6 = input().strip().lower()
    final_result = sorted_by_currency
    while True:
        if "да" in user_input_5 or "нет" in user_input_5:
            if "да" in user_input_6:

                """Программа фильтрует список транзакций по определенному слову в описании"""

                print("\nВведите критерий для поиска\n")
                user_input_7 = input().strip().lower()
                final_result = search_operation_by_description(sorted_by_currency, user_input_7)
            break  # выход из цикла при успешном вводе
        else:
            print("Введите Да/Нет\n")

    """Программа выводит результат"""

    if final_result == []:
        print("По вашему запросу ничего не найдено")
    else:
        print("\nРаспечатываю итоговый список транзакций...\n")
        print(f"Всего банковских операций в выборке: {len(sorted_by_currency)}\n")

        """Программа маскирует номера карт и сетов, меняет формат даты"""

        for transaction in final_result:
            transaction["date"] = get_date(transaction["date"])
            transaction["to"] = mask_account_card(transaction["to"])
            if pd.isna(transaction["from"]):
                print(
                    f"{transaction['date']} {transaction["description"]}\n"
                    f"{transaction['to']}\n{transaction['amount']}\n"
                )
            else:
                transaction["from"] = mask_account_card(transaction["from"])
                print(
                    f"{transaction['date']} {transaction["description"]}\n"
                    f"{transaction['from']} -> {transaction['to']}\n{transaction['amount']}\n"
                )
