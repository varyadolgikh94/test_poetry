import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize("card_number, expected",
                         [
                             ("5000745328745574", "500074******5574"),
                             ("2202745328747777", "220274******7777"),
                             ("1444567891234567", "144456******4567"),
                         ],
                         )
def test_get_mask_card_number_standart(card_number: str, expected: str):
    """Тестирование правильности маскирования номера карты."""
    assert get_mask_card_number(card_number) == expected


@pytest.mark.parametrize(
    "card_number, expected",
    [
        ("401288881888", "401288**1888"),
        ("4012888818888", "401288***8888"),
        ("37598765432100", "375987****2100"),
        ("375987654321001", "375987*****1001"),
        ("70007922896063610", "700079*******3610"),
        ("700079228960636101", "700079********6101"),
        ("7000792289606361012", "700079*********1012"),
    ],
)
def test_len_get_mask_card_number(card_number, expected):
    """Проверка работы функции на различных входных форматах номеров карт,
     включая граничные случаи и нестандартные длины номеров."""
    assert get_mask_card_number(card_number) == expected


def test_get_mask_card_number_no_number():
    """Проверяет функцию маскировки при отсутствии номера карты."""
    assert get_mask_card_number("") == "Неправильно, введите номер карты"


@pytest.mark.parametrize(
    "acc_number, expected",
    [("73654108430135874305", "** 4305"), ("73654108430135854893", "** 4893")],
)
def test_right_get_mask_account(acc_number, expected):
    """Тестирование правильности маскирования номера счета."""
    assert get_mask_account(acc_number) == expected


@pytest.mark.parametrize(
    "acc_number, expected",
    [
        ("73654108430135854893", "** 4893"),
        ("736541084301358548931231231", "** 1231"),
        ("123123213023002", "** 3002"),
    ],
)
def test_len_get_mask_account(acc_number, expected):
    """Проверка работы функции с различными форматами и длинами номеров счетов."""
    assert get_mask_account(acc_number) == expected


def test_wrong_get_mask_account():
    """Проверка, что функция корректно обрабатывает входные строки,
     где номер счета меньше ожидаемой длины."""
    assert get_mask_account("") == "Неправильно, введите номер счета"

