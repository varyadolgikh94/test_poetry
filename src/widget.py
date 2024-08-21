from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_card_info: str) -> str:
    """Функция, которая соответствующим образом маскирует входные данные."""
    info_list: list[str] = account_card_info.split()

    if not info_list[-1].isdigit() and info_list[0].lower() == "счет":
        return "Номер счета не может быть пустым"
    elif not info_list[-1].isdigit():
        return "Номер карты не может быть пустым"
    elif not info_list[0].isalpha():
        return "Тип (счет или карта) не может быть пустым."
    else:

        if info_list[0].lower() == "счет":
            return " ".join(info_list[:-1]) + " " + get_mask_account(info_list[-1])
        elif len(info_list) > 3:
            card_number = [i for i in info_list if i.isdigit()]
            card_name = [i for i in info_list if i.isalpha()]
            return " ".join(card_name) + " " + get_mask_card_number("".join(card_number))
        else:
            return " ".join(info_list[:-1]) + " " + get_mask_card_number(info_list[-1])


def get_date(my_date: str) -> str:
    """Функция форматирования даты."""
    if my_date:
        try:
            formated_date = str(datetime.fromisoformat(my_date))[:10].split("-")
        except ValueError:
            raise ValueError("Дата должна быть в формате YYYY-MM-DD")
        else:
            if datetime.fromisoformat(my_date).year < 1900 or datetime.fromisoformat(my_date).year > 2100:
                return "Дата должна быть между 1900 и 2100 годами."
            return ".".join(formated_date[::-1])
    return "Дата не может быть пустой."
