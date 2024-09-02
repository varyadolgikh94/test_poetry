def filter_by_currency(transactions_list, currency):
    """Функция, которая фильтрует транзакции в указанной валюте."""
    filtered_transactions = list(
        filter(
            lambda transaction: transaction.get("operationAmount").get("currency", {}).get("code") == currency,
            transactions_list,
        )
    )

    if not transactions_list or len(filtered_transactions) == 0:
        return "Нет транзакций в такой валюте"

    return iter(filtered_transactions)


def transaction_descriptions(transactions_list):
    """Функция, которая по очереди возвращает описание каждой транзакции."""
    if not transactions_list:
        yield "Транзакции не найдены"

    descriptions = (
        transaction.get("description", "Описание операции не определено") for transaction in transactions_list
    )
    for description in descriptions:
        yield description


def card_number_generator(start, stop):
    """Функция, генерирующая номера карт в указанном диапазоне."""
    min_number, max_number = 1, 9999999999999999
    if start > stop:
        yield "Минимальный диапазон должен быть меньше максимального."
    elif start < min_number or stop > max_number:
        yield "Диапазон должен быть между 1 и 9999999999999999"

    for i in range(start, stop + 1):
        number_str = "{:016}".format(min_number + i - 1)
        yield " ".join([number_str[x: x + 4] for x in range(0, len(number_str), 4)])
