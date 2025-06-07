import json
import logging
from typing import Any

utils_log = logging.getLogger("utils")
file_handler = logging.FileHandler(
    r"C:\Users\Admin\PycharmProjects\PythonProject\logs\utils.log", "w", encoding="UTF-8"
)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
utils_log.addHandler(file_handler)
utils_log.setLevel(logging.DEBUG)


def get_data_from_json_file(path: str) -> list[dict[Any, Any]]:
    """Принимает на вход путь до JSON-файла и возвращает список словарей
    с данными о финансовых транзакциях."""
    try:
        utils_log.info(f"Открытие файла {path}")
        with open(path, encoding="utf-8") as json_data:
            utils_log.info(f"Десериализация файла {path}")
            transactions_data = json.load(json_data)
            utils_log.info("Возврат пайтон-данных из json-файла ")
            return transactions_data
    except FileNotFoundError:
        utils_log.error(f"Возникла ошибка. {path} не найден")
        print("Файл не найден")
        return [{}]
    except json.JSONDecodeError:
        utils_log.error(f"Возникла ошибка. Формат данных {path} неверный")
        print("Invalid JSON data.")
        return [{}]
