from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(type_number_account_card: str) -> str:
    """Функция принимает тип и номер карты, и счета, возвращает замаскированный номер"""

    str_alpha = ""
    str_number = ""
    for i in type_number_account_card:
        if i.isdigit():
            str_number += i
        else:
            str_alpha += i

    if len(str_number) == 16:
        return f"{str_alpha} {get_mask_card_number(str_number)}"

    else:
        return f"{str_alpha} {get_mask_account(str_number)}"


def get_date(data: str) -> str:
    """Функция даты в формате "ДД.ММ.ГГГГ" """

    return ".".join(data[0:10].split("-"))
