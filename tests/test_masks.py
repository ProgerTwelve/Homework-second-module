from typing import Union

import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "x, expected",
    [
        ("1234567890128756", "1234 56** **** 8756"),
        ("7645290587364512", "7645 29** **** 4512"),
        ("5690873618463826", "5690 87** **** 3826"),
        (6740377957499483, "6740 37** **** 9483"),
    ],
)
def test_get_mask_card_number(x: Union[int, str], expected: str) -> None:
    assert get_mask_card_number(x) == expected


def test_get_mask_card_number_invalid_value() -> None:
    with pytest.raises(ValueError):
        get_mask_card_number("6767 6767 6767 4537")
        get_mask_card_number("")
        get_mask_card_number(9)


def test_get_mask_card_number_invalid_type() -> None:
    with pytest.raises(TypeError):
        get_mask_card_number([12127694])
        get_mask_card_number({"1122": 322})
        get_mask_card_number((1, 2, 3))


@pytest.mark.parametrize(
    "x, expected",
    [
        ("46385610985734647398", "**7398"),
        (65109329849398213749, "**3749"),
        ("00000000000000000000", "**0000"),
        ("99999999999999999999", "**9999"),
    ],
)
def test_get_mask_account(x: Union[int, str], expected: str) -> None:
    assert get_mask_account(x) == expected


def test_get_mask_account_invalid_value() -> None:
    with pytest.raises(ValueError):
        get_mask_account("885643983")
        get_mask_account(0000000000)
        get_mask_account("")


def test_get_mask_account_invalid_type() -> None:
    with pytest.raises(TypeError):
        get_mask_account([])
        get_mask_account((1, 1))
        get_mask_account({"111": 22})
