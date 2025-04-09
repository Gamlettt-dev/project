from unittest.mock import patch

import pytest
import requests

from src.external_api import convert_transaction_to_rub

# Тестовые данные
RUB_TRANSACTION = {
    'operationAmount': {
        'amount': '100.0',
        'currency': {'code': 'RUB'}
    }
}

USD_TRANSACTION = {
    'operationAmount': {
        'amount': '10.0',
        'currency': {'code': 'USD'}
    }
}

INVALID_TRANSACTION = {
    'operationAmount': {
        'currency': {'code': 'USD'}
    }
}


# Тест для RUB транзакции (без конвертации)
@patch.dict('os.environ', {'API_KEY': 'test_key'})
def test_rub_transaction_no_conversion():
    """Должен вернуть ту же сумму, так как валюта уже в RUB"""
    result = convert_transaction_to_rub(RUB_TRANSACTION)
    assert result == 100.0


# Тест для ошибки - нет поля amount
def test_missing_amount_field():
    """Должен вызвать ошибку если нет amount"""
    with pytest.raises(ValueError) as error:
        convert_transaction_to_rub(INVALID_TRANSACTION)
    assert "must contain 'amount'" in str(error.value)


# Тест для ошибки - нет API ключа
@patch.dict('os.environ', {})  # Пустые переменные окружения
def test_missing_api_key():
    """Должен вызвать ошибку если нет API_KEY"""
    with pytest.raises(ValueError) as error:
        convert_transaction_to_rub(USD_TRANSACTION)
    assert "API_KEY not found" in str(error.value)


# Тест для ошибки API
@patch.dict('os.environ', {'API_KEY': 'test_key'})
@patch('requests.get')
def test_api_request_fails(mock_get):
    """Должен пробросить ошибку если API не отвечает"""
    mock_get.side_effect = requests.exceptions.RequestException("API error")
    with pytest.raises(requests.exceptions.RequestException):
        convert_transaction_to_rub(USD_TRANSACTION)
