import pytest

from src.widget import get_date, mask_account_card


def test_mask_account_card():
    """Тестирует стандартную маскировку номеров карт и счетов."""
    assert mask_account_card("Visa Platinum 7000792289606361") == "Visa Platinum 700079******6361"
    assert mask_account_card("Счет 73654108430135874305") == "Счет ** 4305"


@pytest.mark.parametrize(
    "account_card_number, expected",
    [
        ("Maestro 159683785199", "Maestro 159683**5199"),
        ("Счет 64686473678894779589", "Счет ** 9589"),
        ("Visa Classic 6831 9824 7673 7658 01", "Visa Classic 683198********5801"),
        ("MasterCard 375987654321001", "MasterCard 375987*****1001"),
        ("Visa Platinum 8990 9221 1366 5229", "Visa Platinum 899092******5229"),
    ],
)
def test_mask_account_card_nonstandard_number(account_card_number: str, expected: str):
    """Тестирует нестандартную маскировку номеров карт и счетов."""
    assert mask_account_card(account_card_number) == expected


def test_mask_account_card_no_number_or_type():
    """Проверяет функцию маскировки, когда имя или номер карты/счета отсутствуют."""
    assert mask_account_card("Счет") == "Номер счета не может быть пустым"
    assert mask_account_card("Visa Platinum") == "Номер карты не может быть пустым"
    assert mask_account_card("159683785199") == "Тип (счет или карта) не может быть пустым."


def test_get_date():
    """Тестирует стандартное форматирование даты."""
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"


@pytest.mark.parametrize(
    "my_date, expected",
    [
        ("20240311", "11.03.2024"),
        ("2024-03-11", "11.03.2024"),
        ("20050809T183142", "09.08.2005"),
        ("20050809T183142+03", "09.08.2005"),
        ("2005-08-09T18:31:42-03", "09.08.2005"),
        ("20050809T183142+0330", "09.08.2005"),
        ("2005-08-09T18:31:42-03:30", "09.08.2005"),
        ("2005-08-09T18:31:42.201", "09.08.2005"),
    ],
)
def test_get_date_different_formats(my_date: str, expected: str):
    """Тестирует различное форматирование даты по стандарту ISO."""
    assert get_date(my_date) == expected


def test_get_date_no_date():
    """Адекватность даты испытаний."""
    assert get_date("18990809T183142") == "Дата должна быть между 1900 и 2100 годами."
    assert get_date("21010809T183142") == "Дата должна быть между 1900 и 2100 годами."


def test_get_date_wrong_date():
    """Тестирует функцию форматирования даты, когда дата не передается."""
    assert get_date("") == "Дата не может быть пустой."


@pytest.mark.parametrize(
    "my_date",
    [
        "2019-07T18:35:29.512364",
        "2019.07T18:35:29.512364",
        "202403",
    ],
)
def test_get_date_wrong_date_format(my_date: str):
    """Тестирует функцию форматирования даты с неправильным форматом дат, не соответствующим стандарту ISO."""
    with pytest.raises(ValueError, match="Дата должна быть в формате YYYY-MM-DD"):
        get_date(my_date)
