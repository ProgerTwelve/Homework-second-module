from typing import Union

import pytest

from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


def test_filter_by_currency(transactions: list) -> None:
    filter_generator = filter_by_currency(transactions, "USD")
    assert next(filter_generator) == {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }
    assert next(filter_generator) == {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    }


def test_filter_by_currency_invalid_data(invalid_transactions: list) -> None:
    filter_gen_1 = filter_by_currency([], "USD")
    filter_gen_2 = filter_by_currency(invalid_transactions, "USD")
    with pytest.raises(StopIteration):
        next(filter_gen_1)
        next(filter_gen_2)


@pytest.mark.parametrize(
    "list_with_transactions, expected",
    [
        (
            [
                {
                    "id": 939719570,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                    "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод организации",
                    "from": "Счет 75106830613657916952",
                    "to": "Счет 11776614605963066702",
                }
            ],
            "Перевод организации",
        ),
        (
            [
                {
                    "id": 142264268,
                    "state": "EXECUTED",
                    "date": "2019-04-04T23:20:05.206878",
                    "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод со счета на счет",
                    "from": "Счет 19708645243227258542",
                    "to": "Счет 75651667383060284188",
                }
            ],
            "Перевод со счета на счет",
        ),
        (
            [
                {
                    "id": 142264226,
                    "state": "EXECUTED",
                    "date": "2019-02-02T22:21:05.206677",
                    "operationAmount": {"amount": "78211.93", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод со счета на карту",
                    "from": "Счет 19708645243227258542",
                    "to": "Счет 75651667383060284188",
                }
            ],
            "Перевод со счета на карту",
        ),
        (
            [
                {
                    "id": 142264546,
                    "state": "EXECUTED",
                    "date": "2020-04-01T20:10:13.206543",
                    "operationAmount": {"amount": "32111.76", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод со счета на счет",
                    "from": "Счет 19708645243227258542",
                    "to": "Счет 75651667383060284188",
                }
            ],
            "Перевод со счета на счет",
        ),
    ],
)
def test_transaction_descriptions(list_with_transactions: list, expected: str) -> None:
    generator_descriptions = transaction_descriptions(list_with_transactions)
    assert next(generator_descriptions) == expected


def test_transaction_descriptions_invalid_data(invalid_transactions_2: list) -> None:
    generator_invalid_data = transaction_descriptions(invalid_transactions_2)
    generator_invalid_data_2 = transaction_descriptions([])
    with pytest.raises(StopIteration):
        next(generator_invalid_data)
        next(generator_invalid_data_2)


def test_card_number_generator() -> None:
    result_card = card_number_generator(1, 5)
    assert next(result_card) == "0000 0000 0000 0001"
    assert next(result_card) == "0000 0000 0000 0002"
    assert next(result_card) == "0000 0000 0000 0003"
    assert next(result_card) == "0000 0000 0000 0004"
    assert next(result_card) == "0000 0000 0000 0005"


@pytest.mark.parametrize(
    "start, stop, expected",
    [
        ([1, 2, 3], "2221144", TypeError("Неверный тип данных!")),
        ([], {11: "Hello"}, TypeError("Неверный тип данных!")),
    ],
)
def test_card_number_invalid_type(start: list, stop: Union[str, dict], expected: TypeError) -> None:
    card_number_error = card_number_generator(start, stop)
    with pytest.raises(TypeError):
        assert next(card_number_error) == expected


def test_card_number_stop_iteration() -> None:
    card_number_stop = card_number_generator(1, 3)
    with pytest.raises(StopIteration):
        assert next(card_number_stop) == "0000 0000 0000 0001"
        assert next(card_number_stop) == "0000 0000 0000 0002"
        assert next(card_number_stop) == "0000 0000 0000 0003"
        assert next(card_number_stop) == "Элементы итерации закончены"
