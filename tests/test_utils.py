import unittest
from unittest.mock import mock_open, patch

from src.utils import load_transactions_from_json


class TestLoadTransactionsFromJson(unittest.TestCase):

    @patch("builtins.open", new_callable=mock_open, read_data='[{"id": 1, "amount": 100}]')
    def test_load_valid_json(self, mock_file):
        """Тестирование загрузки корректного JSON файла со списком транзакций"""
        result = load_transactions_from_json("dummy_path.json")
        self.assertEqual(result, [{"id": 1, "amount": 100}])
        mock_file.assert_called_once_with("dummy_path.json", "r", encoding="utf-8")

    @patch("builtins.open", side_effect=FileNotFoundError)
    def test_file_not_found(self, mock_file):
        """Тестирование случая, когда файл не найден"""
        result = load_transactions_from_json("nonexistent.json")
        self.assertEqual(result, [])
        mock_file.assert_called_once_with("nonexistent.json", "r", encoding="utf-8")

    @patch("builtins.open", new_callable=mock_open, read_data='invalid json')
    def test_invalid_json(self, mock_file):
        """Тестирование случая с некорректным JSON"""
        result = load_transactions_from_json("invalid.json")
        self.assertEqual(result, [])
        mock_file.assert_called_once_with("invalid.json", "r", encoding="utf-8")

    @patch("builtins.open", new_callable=mock_open, read_data='[]')
    def test_empty_list(self, mock_file):
        """Тестирование пустого списка транзакций"""
        result = load_transactions_from_json("empty.json")
        self.assertEqual(result, [])
        mock_file.assert_called_once_with("empty.json", "r", encoding="utf-8")
