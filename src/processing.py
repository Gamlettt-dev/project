from typing import Dict, List, Union


def filter_by_state(
    data_state: List[Dict[str, Union[int, str, bool]]], state: str = "EXECUTED"
) -> List[Dict[str, Union[int, str, bool]]]:
    """
    Фильтрует список словарей по значению ключа 'state'.

    """
    filtered_data = []
    for item in data_state:
        if item.get("state") == state:
            filtered_data.append(item)
    return filtered_data


def sort_by_date(
    data: List[Dict[str, Union[int, str, bool]]], reverse: bool = True
) -> List[Dict[str, Union[int, str, bool]]]:
    """
    Сортирует список словарей по ключу 'date'.

    """
    sorted_data = sorted(data, key=lambda item: item["date"], reverse=reverse)
    return sorted_data
