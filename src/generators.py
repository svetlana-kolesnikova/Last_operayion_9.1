def card_number_generator(start: int, end: int) -> str:
    """Функция-генератор для создания номеров банковских карт"""
    for num in range(start, end):
        num_card = str(num).zfill(16)
        yield f"{num_card[0:4]} {num_card[4:8]} {num_card[8:12]} {num_card[12:]}"


transactions = [{
          "id": 939719570,
          "state": "EXECUTED",
          "date": "2018-06-30T02:08:58.425572",
          "operationAmount": {
              "amount": "9824.07",
              "currency": {
                  "name": "USD",
                  "code": "USD"
              }
          },
          "description": "Перевод организации",
          "from": "Счет 75106830613657916952",
          "to": "Счет 11776614605963066702"
      },
       {
              "id": 142264265,
              "state": "EXECUTED",
              "date": "2019-04-04T23:20:05.206878",
              "operationAmount": {
                  "amount": "79114.93",
                  "currency": {
                      "name": "USD",
                      "code": "RUB"
                  }
              },
              "description": "Перевод со счета на счет",
              "from": "Счет 19708645243227258542",
              "to": "Счет 75651667383060284188"
       },
      {
              "id": 142264268,
              "state": "EXECUTED",
              "date": "2019-04-04T23:20:05.206878",
              "operationAmount": {
                  "amount": "79114.93",
                  "currency": {
                      "name": "USD",
                      "code": "USD"
                  }
              },
              "description": "Перевод со счета на счет",
              "from": "Счет 19708645243227258542",
              "to": "Счет 75651667383060284188"
       }
        ]


def filter_by_currency(transactions: list, currency: str) -> dict:
    """Функция возвращает итератор, возвращающий поочередно транзакции с заданной валютой"""
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency:
            yield transaction

# usd_transactions = filter_by_currency(transactions, "USD")
# for _ in range(4):
#     # if _:
#     print(next(usd_transactions))
#     # else:
#     #     raise StopIteration("Stop")


