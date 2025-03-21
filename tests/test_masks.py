import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "card_number, expected",
    [
        ("1234567890123456", "1234 56** **** 3456"),
        ("9876543210987654", "9876 54** **** 7654"),
    ],
)
def test_get_mask_card_number(card_number: str, expected: str) -> None:
    assert get_mask_card_number(card_number) == expected


def test_get_mask_card_number_invalid_length() -> None:
    with pytest.raises(ValueError):
        get_mask_card_number("1234567890")


@pytest.mark.parametrize(
    "account_number, expected",
    [
        ("1234567890", "**7890"),
        ("9876543210", "**3210"),
    ],
)
def test_get_mask_account(account_number: str, expected: str) -> None:
    assert get_mask_account(account_number) == expected
