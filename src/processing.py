from typing import Any


def filter_by_state(list_of_dicts: list[dict[str, Any]], state: str = "EXECUTED") -> list[dict[str, Any]]:
    """Функция возвращает новый список словарей, содержащий только те словари, у которых ключ
    state соответствует указанному значению"""

    for i in list_of_dicts:
        if i.get("state"):
            filtered_list = [i for i in list_of_dicts if i.get("state") == state]
            return filtered_list
        else:
            raise ValueError("Ключ state не найден!")


def sort_by_date(lst: list, key_sort: bool = True) -> list:
    """ Функция принимает список словарей и необязательный параметр
    и возвращает новый список, отсортированный по дате (date)."""
    new_list = sorted(lst, key=lambda x: x.get("date"), reverse=key_sort)
    return new_list
