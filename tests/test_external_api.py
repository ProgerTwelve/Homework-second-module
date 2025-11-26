from unittest.mock import patch

from src.external_api import get_transaction_amount


def test_get_transaction_amount_rub(data_for_external_api: list[dict]) -> None:
    assert get_transaction_amount(data_for_external_api) == 9824.07


@patch("requests.request")
def test_get_transaction_amount_usd(mock_requests) -> None:
    mock_requests.return_value.json.return_value = {
        "success": True,
        "query": {"from": "USD", "to": "RUB", "amount": 8221.37},
        "info": {"timestamp": 1748810057, "rate": 77.143373},
        "date": "2025-06-01",
        "result": 634224.212481,
    }
    assert (
        get_transaction_amount(
            [
                {
                    "id": 41428829,
                    "state": "EXECUTED",
                    "date": "2019-07-03T18:35:29.512364",
                    "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод организации",
                    "from": "MasterCard 7158300734726758",
                    "to": "Счет 35383033474447895560",
                }
            ]
        )
        == 634224.212481
    )
