from typing import Any
from unittest.mock import patch

from src.utils import get_data_from_json_file


@patch("json.load")
def test_get_data_from_json_file(mock_load: list[dict[Any]]) -> None:
    mock_load.return_value = [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589",
        }
    ]

    assert get_data_from_json_file(r"C:\Users\Admin\PycharmProjects\PythonProject\data\operations.json") == [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589",
        }
    ]


def test_get_data_from_json_file_invalid_path() -> None:
    assert get_data_from_json_file("data/operations") == [{}]
