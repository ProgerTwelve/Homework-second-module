import json
from typing import Any


def get_data_from_json_file(path: str) -> list[dict[Any, Any]]:
    """Принимает на вход путь до JSON-файла и возвращает список словарей
    с данными о финансовых транзакциях."""
    try:
        with open(path, encoding="utf-8") as json_data:
            transactions_data = json.load(json_data)
            return transactions_data
    except FileNotFoundError:
        print("Файл не найден")
        return [{}]
    except json.JSONDecodeError:
        print("Invalid JSON data.")
        return [{}]
