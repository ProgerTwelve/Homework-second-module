from typing import Any, Generator


def filter_by_currency(transactions: list[dict], currency: str) -> Generator[dict, Any, None]:
    """ Функция принимает на вход список словарей, представляющих транзакции.
    Возвращает итератор, который поочередно выдает транзакции,
    где валюта операции соответствует заданной 'currency'"""
    for transaction in transactions:
        if (
            "operationAmount" in transaction
            and "currency" in transaction["operationAmount"]
            and "name" in transaction["operationAmount"]["currency"]
            and transaction["operationAmount"]["currency"]["name"] == currency
        ):
            yield transaction

def transaction_descriptions(transactions_2: list[dict[str, Any]]) -> Any:
    """Принимает список словарей с транзакциями и возвращает описание каждой операции по очереди."""

    try:
        for transaction in transactions_2:
            if transaction.get("description"):
                yield transaction["description"]
    except StopIteration:
        print("Элементы итерации закончены")


def card_number_generator(start_value: int, stop_value: int) -> iter:
    """Генератор, который выдает номера банковских карт в формате 'XXXX XXXX XXXX XXXX',
    где X — цифра номера карты.
    Генератор может сгенерировать номера карт в заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999."""

    if isinstance(start_value, int) and isinstance(stop_value, int):
        try:
            for number in range(start_value, stop_value + 1):
                card_number = str(number).zfill(16)
                yield f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:]}"
        except StopIteration:
            print("Элементы итерации закончены")
    else:
        raise TypeError("Неверный тип данных!")
