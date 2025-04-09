from typing import Dict, List, Iterator, Iterable


def filter_by_currency(transactions: List[Dict], currency_code: str) -> Iterator[Dict]:
    """
    Принимает на вход список словарей, представляющих транзакции и возвращает
     итератор, который поочередно выдает транзакции, где валюта операции
     соответствует заданной (например, USD)
    """
    for transaction in transactions:
        op_amount = transaction.get("operationAmount", {})
        transaction_currency = op_amount.get("currency", {}).get("code")
        if transaction_currency == currency_code:
            yield transaction


if __name__ == "__main__":
    transactions = [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {"amount": "43318.34", "currency": {"name": "RUB", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
    ]

    usd_transactions = filter_by_currency(transactions, "USD")

    for _ in range(2):
        print(next(usd_transactions))


def transaction_descriptions(data_transaction: List[Dict]) -> Iterator[str]:
    """
    Принимает список словарей с транзакциями и возвращает
    описание каждой операции по очереди.
    """
    for transaction in data_transaction:
        yield transaction.get("description", "Описание отсутствует")


data_transaction = [
    {"description": "Перевод организации"},
    {"description": "Перевод со счета на счет"},
    {"description": "Перевод со счета на счет"},
    {"description": "Перевод с карты на карту"},
    {"description": "Перевод организации"},
]

descriptions = transaction_descriptions(data_transaction)
for _ in range(5):
    print(next(descriptions))


def card_number_generator(start: int, end: int) -> Iterator[str]:
    """
    Генератор который выдает номера банковских карт в формате
    XXXX XXXX XXXX XXXX, где X — цифра номера карты.
    """

    current = start
    while current <= end:
        # Преобразуем число в строку и дополняем нулями до 16 цифр
        card_num = str(current).zfill(16)

        # Разбиваем на группы по 4 цифры и объединяем с пробелами
        formatted_num = " ".join([card_num[0:4], card_num[4:8], card_num[8:12], card_num[12:16]])

        yield formatted_num
        current += 1


for card_number in card_number_generator(1, 5):
    print(card_number)