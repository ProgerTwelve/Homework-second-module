import json
import logging
from typing import Any

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    filename="../logs/utils.log",  # Запись логов в папку logs в файл utils.log
    encoding="utf-8",
    filemode="w",
)  # Перезапись файла при каждом запуске

utils_log = logging.getLogger("utils")


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
