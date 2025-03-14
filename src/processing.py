from typing import List, Dict, Any


def filter_by_state(data_state: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    """
    Фильтрует список словарей по значению ключа 'state'.

    """
    filtered_data = []
    for item in data_state:
        if item.get("state") == state:
            filtered_data.append(item)
    return filtered_data


data_state = [
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


def sort_by_date(data: List[Dict[str, Any]], reverse: bool = True) -> List[Dict[str, Any]]:
    """
    Сортирует список словарей по ключу 'date'.

    """
    sorted_data = sorted(data, key=lambda item: item["date"], reverse=reverse)
    return sorted_data


data = [
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
