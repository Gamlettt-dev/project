def get_mask_card_number(card_number: str) -> str:
    """Маскирует номер банковской карты"""
    card_str = str(card_number)

    if len(card_str) != 16:
        raise ValueError("Номер карты некорректный")

    first_six = card_str[:6]
    last_four = card_str[-4:]

    masked_part = "** ****"

    masked_card = f"{first_six[:4]} {first_six[4:6]}{masked_part} {last_four}"

    return masked_card


def get_mask_account(account_number: str) -> str:
    """Маскирует номер счета"""
    account_str = str(account_number)
    return f"**{account_str[-4:]}"
