import os
from typing import Any, Union

import requests
from dotenv import load_dotenv


def get_transaction_amount(transaction_data: list[dict[Any, Any]]) -> Union[float, Any]:
    """Принимает на вход транзакцию и возвращает сумму транзакции (amount) в рублях, тип данных —
    float. Если транзакция была в USD или EUR, происходит обращение к внешнему API
    для получения текущего курса валют и конвертации суммы операции в рубли."""

    load_dotenv()
    api = os.getenv("Exchange_Rates_Data_API")
    code = "RUB"
    if transaction_data[0]["operationAmount"]["currency"]["code"] == "RUB":
        return float(transaction_data[0]["operationAmount"]["amount"])
    else:
        url = (
            f"https://api.apilayer.com/exchangerates_data/convert"
            f"?to={code}&from={transaction_data[0]["operationAmount"]["currency"]["code"]}"
            f"&amount={transaction_data[0]["operationAmount"]["amount"]}"
        )
        headers = {"apikey": api}
        response = requests.request("GET", url, headers=headers)

        return response.json()["result"]
