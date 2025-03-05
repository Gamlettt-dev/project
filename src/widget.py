def mask_account_card(info: str) -> str:
    """
    Маскирует номер карты или счета.
    - Для карт: оставляет первые 4 и последние 4 цифры, остальные заменяет на **.
    - Для счетов: оставляет только последние 4 цифры, остальные заменяет на **.
    """

    last_space_index = info.rfind(' ')

    if last_space_index == -1:
        return info

    account_type = info[:last_space_index]  # Тип карты или "Счет"
    number = info[last_space_index + 1:]  # Номер карты или счета

    if account_type.lower() == 'счет':
        masked_number = '**' + number[-4:]
    else:
        masked_number = f"{number[:4]} {number[4:6]}** **** {number[-4:]}"

    return f"{account_type} {masked_number}"


from datetime import datetime

def get_date(date_str: str) -> str:
    """
    Преобразует дату из формата "2024-03-11T02:26:18.671407" в формат "ДД.ММ.ГГГГ".
    """
    # Преобразуем строку в объект datetime
    date_obj = datetime.fromisoformat(date_str)
    # Форматируем дату в нужный формат
    return date_obj.strftime("%d.%m.%Y")


# Тестируем mask_account_card
print(mask_account_card("Visa Platinum 7000792289606361"))
print(mask_account_card("Счет 73654108430135874305"))
print(mask_account_card("Maestro 1596837868705199"))
print(mask_account_card("Счет 64686473678894779589"))

# Тестируем get_date
print(get_date("2024-03-11T02:26:18.671407"))
print(get_date("2023-12-25T15:30:00.000000"))
