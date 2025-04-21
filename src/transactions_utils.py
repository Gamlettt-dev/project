import re
from collections import Counter

def finder_inf(list_data, input_str):
    """
    Фильтрует список банковских операций, оставляя только те,
    где описание содержит заданную строку (с учётом регистра).
    """
    pattern = re.compile(input_str, re.IGNORECASE)
    filter_list = []
    for item in list_data:
        if any(pattern.search(str(x)) for x in item.keys() | item.values()):
            filter_list.append(item)
    return filter_list


def count_description(transcription_list, list_description):
    """
    Подсчитывает количество операций в каждой заданной категории.
    """
    count = dict(Counter())
    for list_descr in list_description:
        count[list_descr] = 0
        for transcription in transcription_list:
            description = transcription.get('description', '').lower()
            if description == list_descr.lower():
                count[list_descr] += 1
    return count
