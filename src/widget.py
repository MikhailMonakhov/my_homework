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
        # список известных карт, сделанный на случаи, если пользователь сделал опечатку
        card_list = ["maestro", "mastercard", "visa platinum", "visa gold", "visa classic"]
        # тип карты
        card_name = ""
        # номер карты
        card_number = ""
        is_identified = False
        for card in card_list:
            if card in account_card.lower():
                is_identified = True
                for symbol in account_card:
                    if symbol.isalpha() or symbol == " ":
                        card_name += symbol
                for symbol in account_card:
                    if symbol.isdigit():
                        card_number += symbol
        if is_identified is False:
            return "Не удалось опознать"
        masked_card_number = get_mask_card_number(card_number)
        if "Ошибка ввода" in masked_card_number:
            return "Ошибка ввода"
        return card_name + masked_card_number


def get_date(data: str) -> str:
    """
    Функция, которая вырезает из полученной строки определённые отрезки и затем проверяет наличие
    лишних символов, после чего отправляет f-строкой дату в требуемом виде
    """
    if len(data) < 10:
        return "Ошибка: неверный формат данных"
    # год
    year = data[:4]
    # месяц
    month = data[5:7]
    # день
    day = data[8:10]
    if year.isdigit() is not True or month.isdigit() is not True or day.isdigit() is not True:
        return "Ошибка: неверный формат данных"
    if int(month) > 12:
        return "Ошибка: на данный момент, в году всего 12 месяцев"
    if int(day) > 31:
        return "Ошибка: на данный момент, в месяце не может быть больше 31 дня"
    return f"{day}.{month}.{year}"
