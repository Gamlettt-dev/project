import pandas as pd
import os
from typing import List, Dict, Union, Optional
import logging

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Тип для транзакции
Transaction = Dict[str, Union[str, float, int]]


def read_csv_transactions(file_path: str) -> List[Dict]:
    """
    Читает финансовые операции из CSV файла и возвращает список словарей.
    """
    try:
        # Проверка существования файла
        if not os.path.exists(file_path):
            raise ValueError(f"Файл не найден: {file_path}")

        # Проверка прав доступа
        if not os.access(file_path, os.R_OK):
            raise PermissionError(f"Нет прав на чтение файла: {file_path}")

        logger.info(f"Чтение CSV файла: {file_path}")
        df = pd.read_csv(file_path, sep=';')
        return df.to_dict("records")

    except pd.errors.EmptyDataError:
        logger.error(f"CSV файл пуст: {file_path}")
        raise ValueError(f"CSV файл пуст: {file_path}")
    except PermissionError:
        logger.error(f"Нет прав на чтение файла: {file_path}")
        raise
    except Exception as e:
        logger.error(f"Ошибка при чтении CSV: {e}")
        raise ValueError(f"Ошибка при чтении CSV файла: {e}")


def read_excel_transactions(file_path: str) -> List[Dict]:
    """
    Читает финансовые операции из Excel файла (по умолчанию с первого листа) и возвращает список словарей.
    """
    try:
        if not os.path.exists(file_path):
            raise ValueError(f"Файл не найден: {file_path}")

        if not os.access(file_path, os.R_OK):
            raise PermissionError(f"Нет прав на чтение файла: {file_path}")

        logger.info(f"Чтение Excel файла: {file_path}")
        df = pd.read_excel(file_path, engine='openpyxl')

        # Если файл содержит несколько листов, по умолчанию pandas читает первый
        return df.to_dict("records")

    except pd.errors.EmptyDataError:
        logger.error(f"Excel файл пуст: {file_path}")
        raise ValueError(f"Excel файл пуст: {file_path}")
    except PermissionError:
        logger.error(f"Нет прав на чтение файла: {file_path}")
        raise
    except Exception as e:
        logger.error(f"Ошибка при чтении Excel: {e}")
        raise ValueError(f"Ошибка при чтении Excel файла: {e}")


