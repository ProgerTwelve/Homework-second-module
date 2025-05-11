from .masks import get_mask_account, get_mask_card_number


def mask_account_card(account_or_card: str) -> str:
    """Принимает строку с информацией о типе и номере карты или счета
    и возвращает замаскированный номер карты"""

    if isinstance(account_or_card, str):
        account_or_card_split = account_or_card.split()
        if "Счет" in account_or_card:
            account_number = get_mask_account(account_or_card_split[1])
            return f"{account_or_card_split[0]} {account_number}"
        else:
            card_number = get_mask_card_number(account_or_card_split[-1])
            return f'{" ".join(account_or_card_split[:-1])} {card_number}'
    else:
        raise TypeError("Неверный тип данных!")


def get_date(date: str) -> str:
    """Возвращает строку с датой в формате 'ДД.ММ.ГГГГ'"""

    if isinstance(date, str):
        if len(date) == 26:
            return f"{date[8]}{date[9]}.{date[5]}{date[6]}.{date[0]}{date[1]}{date[2]}{date[3]}"
        else:
            raise ValueError("Неверный формат данных!")
    else:
        raise TypeError("Неверный тип данных!")
