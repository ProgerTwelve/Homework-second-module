from typing import Any

def filter_by_state(list_of_dicts: list[dict[str, Any]], state: str = 'EXECUTED') -> list[dict[str, Any]]:
    """Функция возвращает новый список словарей, содержащий только те словари, у которых ключ
state соответствует указанному значению"""

    filtered_list = [i for i in list_of_dicts if i.get("state") == state]

    return filtered_list




