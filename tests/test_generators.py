import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


# Фикстуры
@pytest.fixture
def currency_transactions():
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {"amount": "43318.34", "currency": {"code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
    ]


@pytest.fixture
def description_transactions():
    return [
        {"description": "Перевод организации"},
        {"description": "Перевод со счета на счет"},
        {"description": "Перевод со счета на счет"},
        {"description": "Перевод с карты на карту"},
        {"description": "Перевод организации"},
    ]


# Параметризованные тесты для filter_by_currency
@pytest.mark.parametrize(
    "currency_code, expected_count, expected_ids",
    [("USD", 2, [939719570, 142264268]), ("RUB", 1, [873106923]), ("EUR", 0, []), ("GBP", 0, [])],
)
def test_filter_by_currency(currency_transactions, currency_code, expected_count, expected_ids):
    filtered = list(filter_by_currency(currency_transactions, currency_code))
    assert len(filtered) == expected_count
    assert [t["id"] for t in filtered] == expected_ids


def test_empty_currency_transactions():
    assert list(filter_by_currency([], "USD")) == []


# Параметризованные тесты для transaction_descriptions
@pytest.mark.parametrize(
    "transactions, expected_descriptions",
    [
        pytest.param(
            [
                {"description": "Перевод организации"},
                {"description": "Перевод со счета на счет"},
                {"description": "Перевод с карты на карту"},
            ],
            ["Перевод организации", "Перевод со счета на счет", "Перевод с карты на карту"],
            id="standard_case",
        ),
        pytest.param(
            [{"id": 1}, {"description": "Перевод"}, {"id": 2}],
            ["Описание отсутствует", "Перевод", "Описание отсутствует"],
            id="missing_descriptions",
        ),
        pytest.param([], [], id="empty_list"),
    ],
)
def test_transaction_descriptions_parametrized(transactions, expected_descriptions):
    descriptions = list(transaction_descriptions(transactions))
    assert descriptions == expected_descriptions


# Оригинальные тесты для обратной совместимости
def test_transaction_descriptions(description_transactions):
    descriptions = list(transaction_descriptions(description_transactions))
    assert descriptions == [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
        "Перевод организации",
    ]


def test_generator_behavior(description_transactions):
    gen = transaction_descriptions(description_transactions)
    assert next(gen) == "Перевод организации"
    assert next(gen) == "Перевод со счета на счет"
    assert next(gen) == "Перевод со счета на счет"
    assert next(gen) == "Перевод с карты на карту"
    assert next(gen) == "Перевод организации"
    with pytest.raises(StopIteration):
        next(gen)


# Фикстура для генератора (опционально)
@pytest.fixture
def card_gen():
    def _gen(start, end):
        return list(card_number_generator(start, end))

    return _gen


# Параметризованный тест для проверки генерации и форматирования
@pytest.mark.parametrize(
    "start, end, expected",
    [
        # Обычный диапазон
        (
            1,
            5,
            [
                "0000 0000 0000 0001",
                "0000 0000 0000 0002",
                "0000 0000 0000 0003",
                "0000 0000 0000 0004",
                "0000 0000 0000 0005",
            ],
        ),
        # Одно значение
        (42, 42, ["0000 0000 0000 0042"]),
        # Крайние значения
        (0, 0, ["0000 0000 0000 0000"]),
        (9999999999999999, 9999999999999999, ["9999 9999 9999 9999"]),
        # Большой диапазон
        (
            9999999999999995,
            9999999999999999,
            [
                "9999 9999 9999 9995",
                "9999 9999 9999 9996",
                "9999 9999 9999 9997",
                "9999 9999 9999 9998",
                "9999 9999 9999 9999",
            ],
        ),
        # Числа с ведущими нулями (в исходном числе)
        (123, 123, ["0000 0000 0000 0123"]),
    ],
)
def test_generation_and_formatting(card_gen, start, end, expected):
    """Проверка генерации и форматирования для разных диапазонов."""
    assert card_gen(start, end) == expected


# Параметризованный тест для проверки пустого диапазона
@pytest.mark.parametrize(
    "start, end",
    [
        (10, 1),  # start > end
        (100, -100),  # отрицательные числа (если поддерживаются)
        (5, 4),  # обычный случай пустого диапазона
    ],
)
def test_empty_range(start, end):
    """Проверка, что генератор возвращает пустой список при start > end."""
    assert list(card_number_generator(start, end)) == []


# Параметризованный тест для проверки дополнения нулями
@pytest.mark.parametrize(
    "input_num, expected",
    [
        (1, "0000 0000 0000 0001"),
        (999, "0000 0000 0000 0999"),
        (1234567890123456, "1234 5678 9012 3456"),
        (9999999999999999, "9999 9999 9999 9999"),
    ],
)
def test_leading_zeros(input_num, expected):
    """Проверка, что числа дополняются нулями до 16 цифр."""
    assert next(card_number_generator(input_num, input_num)) == expected
