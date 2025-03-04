from src.masks import get_mask_account, get_mask_card_number

# Пример использования функции
if __name__ == "__main__":
    card_number = 1234567890123456
    account_number = 1234567890

    masked_card = get_mask_card_number(str(card_number))
    masked_account = get_mask_account(str(account_number))

    print(f"Masked card: {masked_card}")
    print(f"Masked account: {masked_account}")
