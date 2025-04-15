from typing import Dict, List, Union

from src.external_api import convert_transaction_to_rub
from src.generators import card_number_generator, filter_by_currency, transaction_descriptions
from src.masks import get_mask_account, get_mask_card_number
from src.processing import filter_by_state, sort_by_date
from src.utils import load_transactions_from_json
from src.widget import get_date, mask_account_card
from src.file_reader import read_csv_transactions, read_excel_transactions
from config import TRANSACTIONS_CSV, TRANSACTIONS_EXCEL

# Пример использования функции
if __name__ == "__main__":
    card_number = 1234567890123456
    account_number = 1234567890

    masked_card = get_mask_card_number(str(card_number))
    masked_account = get_mask_account(str(account_number))

    print(f"Masked card: {masked_card}")
    print(f"Masked account: {masked_account}")

    print(get_date("2024-03-11T02:26:18.671407"))

    card_nums = [
        "Visa Platinum 7000792289606361",
        "Счет 73654108430135874305",
        "Maestro 1596837868705199",
        "Счет 64686473678894779589",
    ]

    for card in card_nums:
        print(mask_account_card(card))

# Проверка загрузки
txs = load_transactions_from_json("data/operations.json")
print(txs)

for i, tx in enumerate(txs, 1):
    print(f"Тест #{i}: {tx}")
    try:
        result = convert_transaction_to_rub(tx)
        print(f"Результат: {result:.2f} RUB\n")
    except Exception as e:
        print(f"Ошибка: {e}\n")


data: List[Dict[str, Union[int, str, bool]]] = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]


# Сортировка по убыванию (по умолчанию)
result_descending = sort_by_date(data)
print(result_descending)


# Сортировка по возрастанию
result_ascending = sort_by_date(data, reverse=False)
print(result_ascending)


data_state: List[Dict[str, Union[int, str, bool]]] = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

# Фильтрация по state='EXECUTED'
result_executed = filter_by_state(data_state)
print(result_executed)

# Фильтрация по state='CANCELED'
result_canceled = filter_by_state(data_state, state="CANCELED")
print(result_canceled)


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


for card_number in card_number_generator(1, 5):
    print(card_number)


    # Чтение CSV
    try:
        csv_data = read_csv_transactions(TRANSACTIONS_CSV)
        print("Данные из CSV:")
        print(f"Всего записей: {len(csv_data)}")
        print("Первые 3 записи:")
        for i, item in enumerate(csv_data[:3], 1):
            print(f"{i}. {item}")
    except Exception as e:
        print(f"Ошибка при чтении CSV: {e}")

    # Чтение Excel
    try:
        excel_data = read_excel_transactions(TRANSACTIONS_EXCEL)
        print("\nДанные из Excel:")
        print(f"Всего записей: {len(excel_data)}")
        print("Первые 3 записи:")
        for i, item in enumerate(excel_data[:3], 1):
            print(f"{i}. {item}")
    except Exception as e:
        print(f"\nОшибка при чтении Excel: {e}")