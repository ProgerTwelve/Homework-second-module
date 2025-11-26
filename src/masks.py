import logging
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
# Создаем путь до файла логов относительно текущей директории
real_file_path = os.path.join(current_dir, "../logs/masks.log")
abs_file_path = os.path.abspath(real_file_path)

masks_log = logging.getLogger("masks")
file_handler = logging.FileHandler(abs_file_path, "w", encoding="UTF-8")
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
masks_log.addHandler(file_handler)
masks_log.setLevel(logging.DEBUG)


def get_mask_card_number(card_number: int) -> str:
    """Функция маскировки банковской карты.
    Принимает на вход номер карты и возвращает ее маску"""

    try:
        masks_log.debug(f"Начало маскировки номера карты: {card_number}")
        my_card_number = str(card_number)
        if len(my_card_number) >= 16:
            card_text = my_card_number[:6] + "*" * (len(my_card_number) - 10) + my_card_number[-4:]
            result = " ".join([card_text[i: i + 4] for i in range(0, len(card_text), 4)])
            masks_log.info(f"Маскировка номера карты успешно завершена {result}")
        else:
            result = my_card_number
            masks_log.error(f"Ошибка, номер карты меньше 16 символов: {result}, маскировка не выполнена.")
        return result
    except Exception as e:
        masks_log.error(f"Ошибка при маскировке номера карты {card_number}: {e}")
        raise


def get_mask_account(account_number: int) -> str:
    """Функция маскировки банковского счета.
    Принимает на вход номер счета и возвращает его маску."""

    try:
        masks_log.debug(f"Начало маскировки номера счета: {account_number}")
        if not isinstance(account_number, int):
            text_error = "Номер счета должен быть целым числом"
            masks_log.error(text_error)
            raise TypeError(text_error)
        account_number_str = str(account_number)
        if len(account_number_str) >= 5:
            result = "**" + account_number_str[-4:]
            masks_log.info(f"Маскировка счета успешно завершена {result}")
        else:
            result = account_number_str
            masks_log.error(f"Ошибка, номер счета меньше 5 символов: {result}, маскировка не выполнена.")
        return result
    except Exception as e:
        masks_log.error(f"Ошибка при маскировке счета: {account_number}: {e}")
        raise
