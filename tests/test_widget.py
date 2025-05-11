import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "x, expected",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Счет 35383033474447895560", "Счет **5560"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
        ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
        ("Счет 73654108430135874305", "Счет **4305"),
    ],
)
def test_mask_account_card(x, expected):
    assert mask_account_card(x) == expected


def test_mask_account_card_invalid_type():
    with pytest.raises(TypeError):
        mask_account_card([])
        mask_account_card(11)


@pytest.mark.parametrize(
    "x, expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2020-08-20T08:30:45.675537", "20.08.2020"),
        ("2025-01-12T32:76:04.875934", "12.01.2025"),
    ],
)
def test_get_date(x, expected):
    assert get_date(x) == expected


def test_get_date_invalid_value():
    with pytest.raises(ValueError):
        get_date("")
        get_date("2024-03")


def test_get_date_invalid_type():
    with pytest.raises(TypeError):
        get_date(["2023-08-23"])
        get_date(20240312)
