import json
import logging
from typing import Dict, List

logger = logging.getLogger('utils')
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler('logs/utils.log', encoding='utf-8')
file_handler.setLevel(logging.DEBUG)
file_formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def load_transactions_from_json(file_path: str) -> List[Dict]:
    """
    Загружает список транзакций из JSON-файла.
    """
    try:
        logger.debug(f"Попытка загрузить данные из файла: {file_path}")

        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

            # Проверяем, что данные - это список
            if isinstance(data, list):
                logger.info(f"Успешно загружено {len(data)} транзакций из файла {file_path}")
                return data

            logger.warning(f"Файл {file_path} не содержит список транзакций")
            return []

    except FileNotFoundError:
        logger.error(f"Файл не найден: {file_path}")
        return []
    except json.JSONDecodeError:
        logger.error(f"Ошибка декодирования JSON в файле: {file_path}")
        return []
