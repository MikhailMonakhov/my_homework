from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_card: str) -> str:
    """
    Функция, которая определяет, получила ли она тип и номер карты или номер счёта, маскирует это и
    возвращает в нужном виде
    """
    if "Счет" in account_card or "Счёт" in account_card:
        # номер счёта
        account_number = ""
        for symbol in account_card:
            if symbol.isdigit():
                account_number += symbol
        masked_account_card = get_mask_account(account_number)
        return "Счет " + masked_account_card
    else:
        # тип карты
        card_name = ""
        for symbol in account_card:
            if symbol.isalpha() or symbol == " ":
                card_name += symbol
        # номер карты
        card_number = ""
        for symbol in account_card:
            if symbol.isdigit():
                card_number += symbol
        masked_card_number = get_mask_card_number(card_number)
        return card_name + masked_card_number


def get_date(data: str) -> str:
    """
    Функция, которая вырезает из полученной строки определённые отрезки и затем проверяет наличие
    лишних символов, после чего отправляет f-строкой дату в требуемом виде
    """
    # год
    year = data[:4]
    # месяц
    month = data[5:7]
    # день
    day = data[8:10]
    if year.isdigit() is not True or month.isdigit() is not True or day.isdigit() is not True:
        return "Ошибка: неверный формат данных"
    else:
        return f"{day}.{month}.{year}"


# test_list = ["Maestro 1596837868705199",
# "Счет 64686473678894779589",
# "MasterCard 7158300734726758",
# "Счет 35383033474447895560",
# "Visa Classic 6831982476737658",
# "Visa Platinum 8990922113665229",
# "Visa Gold 5999414228426353",
# "Счет 73654108430135874305"
# ]
# for i in test_list:
#    print(mask_account_card(i))
