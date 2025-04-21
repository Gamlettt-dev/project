from typing import Dict, List, Union
from pprint import pprint
# Конфигурации и пути к данным
from config import TRANSACTIONS_CSV, TRANSACTIONS_EXCEL, TRANSACTIONS_JSON

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
from src.transactions_utils import finder_inf

def main():
    print("Привет! Добро пожаловать в программу работы c банковскими транзакциями.")
    print("""
    Выберите необходимый пункт меню:
    1. Получить информацию о транзакциях из JSON-файла
    2. Получить информацию о транзакциях из CSV-файла
    3. Получить информацию о транзакциях из XLSX-файла
    """)

    while True:
        file_type = user_input = str(input().lower().strip())
        if user_input == "1":
            print("Вы выбрали JSON-файл")
            break
        elif user_input == "2":
            print("Вы выбрали CSV-файл")
            break
        elif user_input == "3":
            print("Вы выбрали XLSX-файл")
            break
        else:
            print("Введите корректное число.")

    while True:
        print("Введите статус, по которому необходимо выполнить фильтрацию."
              "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING")


        state = input().lower().strip()

        statuses = ["EXECUTED", "CANCELED", "PENDING"]

        if state.upper() in statuses:
            break
        else:
            print(f'Статус операции недоступен {state}')

    while True:
        print("Отсортировать операции по дате? Да/Нет")

        sorted_data = input().lower().strip()

        if sorted_data in ['да','нет']:
            break

    while True:
        print("""Отсортировать -
            1: по возрастанию
            2: по убыванию?
            """)

        sorted_by_data = input().lower().strip()

        if sorted_by_data in ['1','2']:
            break

    while True:
        print("Выводить только рублевые транзакции? Да/Нет")

        currency_rub = input().lower().strip()

        if currency_rub in ['да', 'нет']:
            break

    while True:
        print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")

        word_sort = input().lower().strip()

        if word_sort in 'нет':
            break
        elif word_sort in 'да':
            print("Напишите слово для фильтрации:")

            word = input().lower().strip()

            break

    while True:
        if file_type == '1':
            file = load_transactions_from_json(TRANSACTIONS_JSON)
            break
        elif file_type == '2':
            file = read_csv_transactions(TRANSACTIONS_CSV)
            break
        elif file_type == '3':
            file = read_excel_transactions(TRANSACTIONS_EXCEL)
            break
        else:
            print('Введите число от 1-3')

    transactions = filter_by_state(file, state)
    # Сортировка по дате
    if sorted_data == "да":
        revers_order = sorted_data == "по убыванию"
        transactions = sort_by_date(transactions, reverse=revers_order)

    # Фильтрация по валюте
    if filter_by_state == "да":
        transactions = list(filter_by_currency(transactions, "RUB"))
    else:
        user_currency = (input("Введите слово для фильтрации валюты: USD, EUR: ")).upper().strip()
        transactions = list(filter_by_currency(transactions, user_currency))

    # Фильтрация по описанию
    if word_sort == "да":
        search_word = (input("Введите ключевое слово для поиска: ")).lower().strip()
        transactions = finder_inf(transactions, search_word)

    print("Распечатываю итоговый список транзакций...")
    print(f"Всего банковских операций в выборке {len(transactions)}")

    for transaction in transactions:
        # Безопасное извлечение данных с проверкой ключей
        date = get_date(transaction.get("date", "Дата неизвестна"))
        description = transaction.get("description", "Описание отсутствует")
        from_account = mask_account_card(transaction.get("from", ""))  # Маскируем "откуда"
        to_account = mask_account_card(transaction.get("to", ""))  # Маскируем "куда"

        # Обработка вложенной структуры operationAmount
        operation_amount = transaction.get("operationAmount", {})
        amount = operation_amount.get("amount", "Сумма не указана")
        currency = operation_amount.get("currency", {})
        currency_code = currency.get("code", "Валюта не указана")

        # Форматированный вывод
        print(
            f"""
Дата: {date} {description}
{from_account} -> {to_account}
Сумма: {amount} {currency_code}
    """
        )


if __name__ == "__main__":
    main()

