from typing import Union


def get_mask_card_number(card_number: Union[int, str]) -> str:
    """Маскирует номер банковской карты в формате 0000 00** **** 0000"""

    if isinstance(card_number, int) or isinstance(card_number, str):
        str_number = str(card_number)
        if len(str_number) == 16:
            str_card_number = str_number[0:4] + " " + str_number[4:6] + "** **** " + str_number[-4:]
            return str_card_number
        else:
            raise ValueError("Неверный формат данных!")
    else:
        raise TypeError("Неверный тип данных!")


def get_mask_account(account: Union[int, str]) -> str:
    """Маскирует номер банковского счета в формате **0000"""

    if isinstance(account, int) or isinstance(account, str):
        str_account = str(account)
        if len(str_account) == 20:
            return "**" + str_account[-4:]
        else:
            raise ValueError("Неверный формат данных!")
    else:
        raise TypeError("Неверный тип данных!")
