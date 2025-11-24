import re
from collections import Counter


def process_bank_search(data:list[dict], search:str)->list[dict]:
    """Принимает список словарей с данными о банковских операциях и строку поиска,
    а возвращает список словарей, у которых в описании есть данная строка."""

    found_list = []
    for d in data:
        if re.search(search, d["description"], flags=re.IGNORECASE):
            found_list.append(d)

    return found_list

def process_bank_operations(data:list[dict], categories:list[str]) -> dict[str, int]:
    """Принимает список словарей с данными о банковских операциях и список категорий.
    Возвращает словарь, где ключи — названия категорий, значения — количество операций,
    в которых description содержит соответствующую категорию (подстроку)."""

    # Список для накопления найденных категорий
    matched_categories = []

    # Проходим по каждой операции в данных
    for operation in data:
        try:
            description = operation.get("description", "").upper()  # Приводим к нижнему регистру
            # Проверяем каждую категорию
            for category in categories:
                if category.upper() in description:
                    matched_categories.append(category)
        except Exception as e:
            # пропускаем
            matched_categories.append("")

    # Создаём Counter из найденных категорий
    counter = Counter(matched_categories)

    # Инициализируем результат со всеми категориями (включая те, что не встретились)
    result = {category: counter.get(category, 0) for category in categories}

    return result