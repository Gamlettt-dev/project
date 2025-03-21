import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "info, expected",
    [
        ("Счет 1234567890123456", "Счет **3456"),
        ("Visa Platinum 1234567890123456", "Visa Platinum 1234 56** **** 3456"),
        ("MasterCard 1234567890123456", "MasterCard 1234 56** **** 3456"),
    ],
)
def test_mask_account_card_valid(info: str, expected: str) -> None:
    assert mask_account_card(info) == expected


def test_mask_account_card_invalid_input() -> None:
    assert mask_account_card("InvalidInput") == "InvalidInput"


@pytest.mark.parametrize(
    "date_str, expected",
    [
        ("2019-07-03T18:35:29.512364", "03.07.2019"),
        ("2018-06-30T02:08:58.425572", "30.06.2018"),
        ("2020-01-01T00:00:00.000000", "01.01.2020"),
    ],
)
def test_get_date_valid(date_str: str, expected: str) -> None:
    assert get_date(date_str) == expected
