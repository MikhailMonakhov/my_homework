from typing import Union


def get_mask_card_number(card_number: Union[str, int]) -> str:
    """
    Функция, которая получает номер карты, проверяет длину и наличие неправильных знаков,
    делит на 4 равные части, маскируя нужные отрезки, и возвращает f-строкой замаскированный номер карты
    """
    card_number_str = str(card_number)
    card_number_without_spaces = card_number_str.replace(" ", "")
    if len(card_number_without_spaces) != 16 or card_number_without_spaces.isdigit() is not True:
        print("В номере банковской карты содержатся неправильные знаки или неправильное количество знаков.")
        # добавил просто из-за предупреждения о разности результатов в аннотации и в return
        # (ожидает str, получает None в случае отсутствия строки ниже)
        return "Ошибка ввода"
    else:
        card_number_part_1 = card_number_without_spaces[:4]
        card_number_part_2 = card_number_without_spaces[4:6] + "**"
        card_number_part_3 = "****"
        card_number_part_4 = card_number_without_spaces[-4:]
        return f"{card_number_part_1} {card_number_part_2} {card_number_part_3} {card_number_part_4}"


def get_mask_account(account_number: Union[str, int]) -> str:
    """
    Функция, которая получает номер счёта, проверяет наличие неправильных знаков и возвращает
    в нужном формате последние 4 цифры номера
    """
    account_number_str = str(account_number)
    account_number_without_spaces = account_number_str.replace(" ", "")
    if account_number_without_spaces.isdigit() is not True:
        print("В номере банковского счёта содержатся неправильные знаки.")
        # аналогично комментарию в строках 13-14
        return "Ошибка ввода"
    else:
        masked_account_number = account_number_without_spaces[-4:]
        return "**" + masked_account_number
