from unittest.mock import mock_open, patch

import pandas as pd

from src.file_reader import read_csv_transactions, read_excel_transactions


@patch("builtins.open", new_callable=mock_open, read_data="id;amount;state\n1;1000.0;EXECUTED")
@patch("os.path.exists", return_value=True)
@patch("os.access", return_value=True)
@patch("pandas.read_csv")
def test_read_csv_transactions(mock_read_csv, mock_access, mock_exists, mock_file):
    mock_df = pd.DataFrame([{"id": 1, "amount": 1000.0, "state": "EXECUTED"}])
    mock_read_csv.return_value = mock_df

    result = read_csv_transactions("fake/path.csv")

    assert isinstance(result, list)
    assert result[0]["id"] == 1
    assert result[0]["amount"] == 1000.0
    assert result[0]["state"] == "EXECUTED"


@patch("os.path.exists", return_value=True)
@patch("os.access", return_value=True)
@patch("pandas.read_excel")
def test_read_excel_transactions(mock_read_excel, mock_access, mock_exists):
    mock_df = pd.DataFrame([
        {"id": 2, "amount": 5000.0, "state": "CANCELED"}
    ])
    mock_read_excel.return_value = mock_df

    result = read_excel_transactions("fake/path.xlsx")

    assert isinstance(result, list)
    assert result[0]["id"] == 2
    assert result[0]["amount"] == 5000.0
    assert result[0]["state"] == "CANCELED"
