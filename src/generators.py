from typing import Dict, Iterator, List


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


def transaction_descriptions(data_transaction: List[Dict]) -> Iterator[str]:
    """
    Принимает список словарей с транзакциями и возвращает
    описание каждой операции по очереди.
    """
    for transaction in data_transaction:
        yield transaction.get("description", "Описание отсутствует")


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
