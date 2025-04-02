from datetime import datetime


def mask_account_card(info: str) -> str:
    """
    Маскирует номер карты или счета.
    - Для карт: оставляет первые 4 и последние 4 цифры, остальные заменяет на **.
    - Для счетов: оставляет только последние 4 цифры, остальные заменяет на **.
    """

    last_space_index = info.rfind(" ")

    if last_space_index == -1:
        return info

    account_type = info[:last_space_index]  # Тип карты или "Счет"
    number = info[last_space_index + 1 :]  # Номер карты или счета

    if account_type.lower() == "счет":
        masked_number = "**" + number[-4:]
    else:
        masked_number = f"{number[:4]} {number[4:6]}** **** {number[-4:]}"

    return f"{account_type} {masked_number}"


def get_date(date_str: str) -> str:
    """
    Преобразует дату из формата "2024-03-11T02:26:18.671407" в формат "ДД.ММ.ГГГГ".
    """
    # Преобразуем строку в объект datetime
    date_obj = datetime.fromisoformat(date_str)
    # Форматируем дату в нужный формат
    return date_obj.strftime("%d.%m.%Y")
