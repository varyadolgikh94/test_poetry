import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency(transactions):
    """Тестирует функцию filter_by_currency с разными передаваемыми параметрами."""
    usd_transactions = filter_by_currency(transactions, "USD")
    assert next(usd_transactions) == {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }
    assert next(usd_transactions) == {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    }
    rub_transactions = filter_by_currency(transactions, "RUB")
    assert next(rub_transactions) == {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    }


def test_filter_by_currency_no_transactions(transactions):
    """Тестирует функцию filter_by_currency без транзакций или без транзакций в выбранной валюте."""
    assert filter_by_currency(transactions, "EUR") == "Нет транзакций в такой валюте"
    assert filter_by_currency([], "USD") == "Нет транзакций в такой валюте"


def test_filter_by_currency_no_currency():
    """Проверяет функцию filter_by_currency, когда валюта операции отсутствует."""
    no_currency_transactions = [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
    ]
    assert filter_by_currency(no_currency_transactions, "USD") == "Нет транзакций в такой валюте"


def test_transaction_descriptions(transactions):
    """Описания тестов последовательного поколения."""
    descriptions = transaction_descriptions(transactions)
    assert next(descriptions, "Больше никаких транзакций") == "Перевод организации"
    assert next(descriptions, "Больше никаких транзакций") == "Перевод со счета на счет"
    assert next(descriptions, "Больше никаких транзакций") == "Перевод со счета на счет"
    assert next(descriptions, "Больше никаких транзакций") == "Перевод с карты на карту"
    assert next(descriptions, "Больше никаких транзакций") == "Перевод организации"
    assert next(descriptions, "Больше никаких транзакций") == "Открытие вклада"
    assert next(descriptions, "Больше никаких транзакций") == "Описание операции не определено"
    assert next(descriptions, "Больше никаких транзакций") == "Больше никаких транзакций"


def test_transaction_descriptions_no_transactions():
    """Генератор описаний тестов без данных о транзакциях."""
    assert next(transaction_descriptions([])) == "Транзакции не найдены"


def test_transaction_descriptions_no_description():
    """Генератор описаний тестируется, когда описания отсутствуют."""
    no_description_transactions = [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
    ]
    assert next(transaction_descriptions(no_description_transactions)) == "Описание операции не определено"
    assert next(transaction_descriptions(no_description_transactions)) == "Описание операции не определено"


def test_card_number_generator():
    """Тесты карточек номеров последовательного поколения."""
    card_number = card_number_generator(1, 5)
    assert next(card_number) == "0000 0000 0000 0001"
    assert next(card_number) == "0000 0000 0000 0002"
    assert next(card_number) == "0000 0000 0000 0003"
    assert next(card_number) == "0000 0000 0000 0004"
    assert next(card_number) == "0000 0000 0000 0005"


@pytest.mark.parametrize(
    "start, stop, expected",
    [
        (
                1000,
                1003,
                [
                    "0000 0000 0000 1000",
                    "0000 0000 0000 1001",
                    "0000 0000 0000 1002",
                    "0000 0000 0000 1003",
                ],
        ),
        (
                10000010,
                10000013,
                [
                    "0000 0000 1000 0010",
                    "0000 0000 1000 0011",
                    "0000 0000 1000 0012",
                    "0000 0000 1000 0013",
                ],
        ),
        (
                100000000100,
                100000000103,
                [
                    "0000 1000 0000 0100",
                    "0000 1000 0000 0101",
                    "0000 1000 0000 0102",
                    "0000 1000 0000 0103",
                ],
        ),
        (
                1000000000001000,
                1000000000001003,
                [
                    "1000 0000 0000 1000",
                    "1000 0000 0000 1001",
                    "1000 0000 0000 1002",
                    "1000 0000 0000 1003",
                ],
        ),
        (
                9999999999999996,
                9999999999999999,
                [
                    "9999 9999 9999 9996",
                    "9999 9999 9999 9997",
                    "9999 9999 9999 9998",
                    "9999 9999 9999 9999",
                ],
        ),
    ],
)
def test_card_number_generator_different_ranges(start, stop, expected):
    """Тестирует генерацию номеров карточек в разных диапазонах."""
    result = list(card_number for card_number in card_number_generator(start, stop))
    assert result == expected


def test_card_number_generator_extreme_numbers():
    """Тестирует генератор чисел карточек с граничными условиями заданного диапазона."""
    assert next(card_number_generator(0, 1)) == "Диапазон должен быть между 1 и 9999999999999999"
    assert next(card_number_generator(1, 10000000000000000)) == "Диапазон должен быть между 1 и 9999999999999999"
    assert next(card_number_generator(1, 0)) == "Минимальный диапазон должен быть меньше максимального."
