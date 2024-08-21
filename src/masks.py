def get_mask_card_number(card_number: str) -> str:
    """Функция маскировки номера банковской карты"""
    if card_number != "":
        num_list = [num for num in card_number]
        open_nums_list = num_list[0:6] + ["*" * (len(num_list) - 10)] + num_list[-4:]
        masked_card_number = "".join(open_nums_list)
        return masked_card_number
    else:
        return "Неправильно, введите номер карты"


def get_mask_account(acc_number: str) -> str:
    """Функция маскировки номера банковского счета"""
    if acc_number != "" and len(acc_number) > 6:
        hidden_num_list = "**", acc_number[-4:]
        hidden_acc_number = " ".join(hidden_num_list)
        return hidden_acc_number
    else:
        return "Неправильно, введите номер счета"
