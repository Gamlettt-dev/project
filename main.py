from typing import Dict, List, Union

# Конфигурации и пути к данным
from config import TRANSACTIONS_CSV, TRANSACTIONS_EXCEL

# Внешние API
from src.external_api import convert_transaction_to_rub

# Чтение данных из файлов
from src.file_reader import read_csv_transactions, read_excel_transactions

# Генераторы
from src.generators import (
    card_number_generator,
    filter_by_currency,
    transaction_descriptions,
)
from src.masks import get_mask_account, get_mask_card_number
from src.processing import filter_by_state, sort_by_date
from src.utils import load_transactions_from_json
from src.widget import get_date, mask_account_card

# Точка входа
if __name__ == "__main__":
    print("Маскирование номера карты и счёта")
    card_number = 1234567890123456
    account_number = 1234567890
    print(f"Masked card: {get_mask_card_number(str(card_number))} (Функция из модуля `src.masks`)")
    print(f"Masked account: {get_mask_account(str(account_number))} (Функция из модуля `src.masks`)\n")

    print("Форматирование даты")
    print(get_date("2024-03-11T02:26:18.671407"), "(Функция из модуля `src.widget`)\n")

    print("Маскирование списка карт и счетов")
    card_nums = [
        "Visa Platinum 7000792289606361",
        "Счет 73654108430135874305",
        "Maestro 1596837868705199",
        "Счет 64686473678894779589",
    ]
    for card in card_nums:
        print(mask_account_card(card), "(Функция из модуля `src.widget`)")
    print()

    print("Загрузка транзакций из JSON")
    txs = load_transactions_from_json("data/operations.json")
    for i, tx in enumerate(txs, 1):
        print(f"Тест #{i}: {tx}")
        try:
            result = convert_transaction_to_rub(tx)
            print(f"Результат: {result:.2f} RUB (Функция из модуля `src.external_api`)\n")
        except Exception as e:
            print(f"Ошибка: {e}\n")

    print("Сортировка транзакций по дате")
    data: List[Dict[str, Union[int, str, bool]]] = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
    print("По убыванию:", sort_by_date(data), "(Функция из модуля `src.processing`)")
    print("По возрастанию:", sort_by_date(data, reverse=False), "(Функция из модуля `src.processing`)", "\n")

    print("Фильтрация по статусу транзакции")
    print("EXECUTED:", filter_by_state(data, state="EXECUTED"), "(Функция из модуля `src.processing`)")
    print("CANCELED:", filter_by_state(data, state="CANCELED"), "(Функция из модуля `src.processing`)", "\n")

    print("Фильтрация по валюте (USD)")
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
        print(next(usd_transactions), "(Функция из модуля `src.generators`)")
    print()

    print("Частота описаний операций")
    data_transaction = [
        {"description": "Перевод организации"},
        {"description": "Перевод со счета на счет"},
        {"description": "Перевод со счета на счет"},
        {"description": "Перевод с карты на карту"},
        {"description": "Перевод организации"},
    ]
    descriptions = transaction_descriptions(data_transaction)
    for _ in range(5):
        print(next(descriptions), "(Функция из модуля `src.generators`)")
    print()

    print("Генерация номеров карт")
    for card_number in card_number_generator(1, 5):
        print(card_number, "(Функция из модуля `src.generators`)")
    print()

    print("Чтение данных из CSV")
    try:
        csv_data = read_csv_transactions(TRANSACTIONS_CSV)
        print(f"Всего записей: {len(csv_data)}")
        print("Первые 3 записи:")
        for i, item in enumerate(csv_data[:3], 1):
            print(f"{i}. {item} (Функция из модуля `src.file_reader`)")
    except Exception as e:
        print(f"Ошибка при чтении CSV: {e}")
    print()

    print("Чтение данных из Excel")
    try:
        excel_data = read_excel_transactions(TRANSACTIONS_EXCEL)
        print(f"Всего записей: {len(excel_data)}")
        print("Первые 3 записи:")
        for i, item in enumerate(excel_data[:3], 1):
            print(f"{i}. {item} (Функция из модуля `src.file_reader`)")
    except Exception as e:
        print(f"Ошибка при чтении Excel: {e}")
