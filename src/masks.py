def get_mask_card_number(card_number: str) -> str | None:
    """Функция маскировки номера банковской карты"""
    if card_number.isdigit() and len(card_number) == 16:
        return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[12:]}"

    else:
        return None


def get_mask_account(acc_number: str) -> str | None:
    """Функция маскировки номера банковского счета"""
    if acc_number.isdigit() and len(acc_number) == 20:
        return f"{'*' * 2}{acc_number[-4::]}"

    else:
        return None


