from typing import Dict, List, Union

import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.fixture
def sample_data() -> List[Dict[str, Union[int, str, bool]]]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.mark.parametrize(
    "state, expected_count",
    [
        ("EXECUTED", 2),
        ("CANCELED", 2),
        ("PENDING", 0),
    ],
)
def test_filter_by_state(
    sample_data: List[Dict[str, Union[int, str, bool]]],
    state: str,
    expected_count: int,
) -> None:

    result: List[Dict[str, Union[int, str, bool]]] = filter_by_state(sample_data, state)
    assert len(result) == expected_count
    for item in result:
        assert item["state"] == state


@pytest.mark.parametrize(
    "reverse, expected_first_id",
    [
        (True, 41428829),
        (False, 939719570),
    ],
)
def test_sort_by_date(
    sample_data: List[Dict[str, Union[int, str, bool]]],
    reverse: bool,
    expected_first_id: int,
) -> None:
    result: List[Dict[str, Union[int, str, bool]]] = sort_by_date(sample_data, reverse=reverse)
    assert result[0]["id"] == expected_first_id
