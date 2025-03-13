from src.masks import get_mask_account, get_mask_card_number
from src.widget import mask_account_card, get_date


# Пример использования функции
if __name__ == "__main__":
    card_number = 1234567890123456
    account_number = 1234567890

    masked_card = get_mask_card_number(str(card_number))
    masked_account = get_mask_account(str(account_number))

    print(f"Masked card: {masked_card}")
    print(f"Masked account: {masked_account}")

    print(get_date("2024-03-11T02:26:18.671407"))

    card_nums = [
        "Visa Platinum 7000792289606361",
        "Счет 73654108430135874305",
        "Maestro 1596837868705199",
        "Счет 64686473678894779589"
    ]

    for card in card_nums:
        print(mask_account_card(card))






