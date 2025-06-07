import logging
from typing import Union

masks_log = logging.getLogger("masks")
file_handler = logging.FileHandler(
    r"C:\Users\Admin\PycharmProjects\PythonProject\logs\masks.log", "w", encoding="UTF-8"
)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
masks_log.addHandler(file_handler)
masks_log.setLevel(logging.DEBUG)


def get_mask_card_number(card_number: Union[int, str]) -> str:
    """Маскирует номер банковской карты в формате 0000 00** **** 0000"""

    masks_log.info(f"Проверка {card_number} на соответствие типу int или str ")
    if isinstance(card_number, int) or isinstance(card_number, str):
        masks_log.info("Проверка успешно пройдена")
        str_number = str(card_number)
        masks_log.info("Проверка длины карты")
        if len(str_number) == 16:
            masks_log.info("Проверка успешно пройдена")
            str_card_number = str_number[0:4] + " " + str_number[4:6] + "** **** " + str_number[-4:]
            masks_log.info(f"Возврат значения {str_card_number}")
            return str_card_number
        else:
            masks_log.error("Проверка провалена. Длина номера карты не 16 чисел")
            raise ValueError("Неверный формат данных!")
    else:
        masks_log.error(f"Проверка провалена. Тип данных {card_number} не является целым числом либо строкой")
        raise TypeError("Неверный тип данных!")


def get_mask_account(account: Union[int, str]) -> str:
    """Маскирует номер банковского счета в формате **0000"""

    masks_log.info(f"Проверка {account} на соответствие типу int или str ")
    if isinstance(account, int) or isinstance(account, str):
        masks_log.info("Проверка успешно пройдена")
        str_account = str(account)
        masks_log.info("Проверка длины символов банковского счета")
        if len(str_account) == 20:
            masks_log.info("Проверка успешно пройдена")
            masks_log.info("Функция успешно вернула замаскированный счет")
            return "**" + str_account[-4:]
        else:
            masks_log.error(f"Проверка {str_account} на длину символов не пройдена ")
            raise ValueError("Неверный формат данных!")
    else:
        masks_log.error(f"Ошибка! {account} не является типом int или str")
        raise TypeError("Неверный тип данных!")
