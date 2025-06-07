from unittest.mock import patch

import pandas
import pandas as pd

from src.csv_excel_data import get_csv_data, get_excel_data


@patch("pandas.read_csv")
def test_get_csv_data(mock_csv: pd.DataFrame) -> None:
    mock_csv.return_value = pd.DataFrame(
        [
            {
                "id": 650703.0,
                "state": "EXECUTED",
                "date": "2023-09-05T11:30:32Z",
                "amount": 16210.0,
                "currency_name": "Sol",
                "currency_code": "PEN",
                "from": "Счет 58803664561298323391",
                "to": "Счет 39745660563456619397",
                "description": "Перевод организации",
            },
            {
                "id": 3598919.0,
                "state": "EXECUTED",
                "date": "2020-12-06T23:00:58Z",
                "amount": 29740.0,
                "currency_name": "Peso",
                "currency_code": "COP",
                "from": "Discover 3172601889670065",
                "to": "Discover 0720428384694643",
                "description": "Перевод с карты на карту",
            },
            {
                "id": 593027.0,
                "state": "CANCELED",
                "date": "2023-07-22T05:02:01Z",
                "amount": 30368.0,
                "currency_name": "Shilling",
                "currency_code": "TZS",
                "from": "Visa 1959232722494097",
                "to": "Visa 6804119550473710",
                "description": "Перевод с карты на карту",
            },
        ]
    )

    assert get_csv_data() == [
        {
            "id": 650703.0,
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "amount": 16210.0,
            "currency_name": "Sol",
            "currency_code": "PEN",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
            "description": "Перевод организации",
        },
        {
            "id": 3598919.0,
            "state": "EXECUTED",
            "date": "2020-12-06T23:00:58Z",
            "amount": 29740.0,
            "currency_name": "Peso",
            "currency_code": "COP",
            "from": "Discover 3172601889670065",
            "to": "Discover 0720428384694643",
            "description": "Перевод с карты на карту",
        },
        {
            "id": 593027.0,
            "state": "CANCELED",
            "date": "2023-07-22T05:02:01Z",
            "amount": 30368.0,
            "currency_name": "Shilling",
            "currency_code": "TZS",
            "from": "Visa 1959232722494097",
            "to": "Visa 6804119550473710",
            "description": "Перевод с карты на карту",
        },
    ]


@patch("pandas.read_excel")
def test_get_excel_data(mock_excel: pd.DataFrame) -> None:
    mock_excel.return_value = pd.DataFrame(
        [
            {
                "id": 2177828.0,
                "state": "EXECUTED",
                "date": "2022-04-14T15:14:21Z",
                "amount": 24853.0,
                "currency_name": "Yuan Renminbi",
                "currency_code": "CNY",
                "from": "Счет 38577962752140632721",
                "to": "Счет 47657753885349826314",
                "description": "Перевод со счета на счет",
            },
            {
                "id": 4137938.0,
                "state": "EXECUTED",
                "date": "2023-01-04T13:13:34Z",
                "amount": 15560.0,
                "currency_name": "Real",
                "currency_code": "BRL",
                "from": "nan",
                "to": "Счет 38164279390569873521",
                "description": "Открытие вклада",
            },
            {
                "id": 4699552.0,
                "state": "EXECUTED",
                "date": "2022-03-23T08:29:37Z",
                "amount": 23423.0,
                "currency_name": "Peso",
                "currency_code": "PHP",
                "from": "Discover 7269000803370165",
                "to": "American Express 1963030970727681",
                "description": "Перевод с карты на карту",
            },
        ]
    )

    assert get_excel_data() == [
        {
            "id": 2177828.0,
            "state": "EXECUTED",
            "date": "2022-04-14T15:14:21Z",
            "amount": 24853.0,
            "currency_name": "Yuan Renminbi",
            "currency_code": "CNY",
            "from": "Счет 38577962752140632721",
            "to": "Счет 47657753885349826314",
            "description": "Перевод со счета на счет",
        },
        {
            "id": 4137938.0,
            "state": "EXECUTED",
            "date": "2023-01-04T13:13:34Z",
            "amount": 15560.0,
            "currency_name": "Real",
            "currency_code": "BRL",
            "from": "nan",
            "to": "Счет 38164279390569873521",
            "description": "Открытие вклада",
        },
        {
            "id": 4699552.0,
            "state": "EXECUTED",
            "date": "2022-03-23T08:29:37Z",
            "amount": 23423.0,
            "currency_name": "Peso",
            "currency_code": "PHP",
            "from": "Discover 7269000803370165",
            "to": "American Express 1963030970727681",
            "description": "Перевод с карты на карту",
        },
    ]
