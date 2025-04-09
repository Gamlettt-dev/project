import json
from typing import Dict, List


def load_transactions_from_json(file_path: str) -> List[Dict]:
    """
    Загружает список транзакций из JSON-файла.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

            # Проверяем, что данные - это список
            if isinstance(data, list):
                return data
            return []

    except (FileNotFoundError, json.JSONDecodeError):
        return []
