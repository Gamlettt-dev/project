import os
from typing import Dict, Any

import requests
from dotenv import load_dotenv

# Загружаем переменные окружения из .env файла
load_dotenv('.env')


def convert_transaction_to_rub(transaction: Dict[str, Any]) -> float:
    """
    Конвертирует сумму транзакции в рубли.
    """
    # Проверяем наличие обязательных полей в operationAmount
    if 'operationAmount' not in transaction:
        raise ValueError("Transaction must contain 'operationAmount' field")

    operation_amount = transaction['operationAmount']
    if not isinstance(operation_amount, dict):
        raise ValueError("operationAmount must be a dictionary")

    if 'amount' not in operation_amount or 'currency' not in operation_amount:
        raise ValueError("operationAmount must contain 'amount' and 'currency' fields")

    try:
        amount = float(operation_amount['amount'])
    except (ValueError, TypeError):
        raise ValueError("Amount must be a number")

    currency_info = operation_amount['currency']
    if not isinstance(currency_info, dict) or 'code' not in currency_info:
        raise ValueError("Currency must be a dictionary with 'code' field")

    currency = currency_info['code']
    if not isinstance(currency, str):
        raise ValueError("Currency code must be a string")

    # Если валюта уже рубли, просто возвращаем сумму
    if currency == 'RUB':
        return amount

    # Поддерживаемые валюты для конвертации
    supported_currencies = ['USD', 'EUR']
    if currency not in supported_currencies:
        raise ValueError(f"Unsupported currency: {currency}")

    # Получаем API ключ из переменных окружения
    api_key = os.getenv('API_KEY')
    if not api_key:
        raise ValueError("API_KEY not found in environment variables")

    # Делаем запрос к API для получения курса валют
    url = f"https://api.apilayer.com/exchangerates_data/latest?base={currency}&symbols=RUB"
    headers = {"apikey": api_key}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Проверяем на ошибки HTTP
        data = response.json()

        if not isinstance(data, dict) or 'rates' not in data:
            raise ValueError("Invalid API response format")

        rates = data['rates']
        if not isinstance(rates, dict) or 'RUB' not in rates:
            raise ValueError("RUB rate not found in response")

        rate = float(rates['RUB'])  # Явное преобразование в float
        return amount * rate

    except requests.exceptions.RequestException as e:
        raise ValueError(f"API request failed: {str(e)}")
    except (ValueError, TypeError) as e:
        raise ValueError(f"Failed to process API response: {str(e)}")