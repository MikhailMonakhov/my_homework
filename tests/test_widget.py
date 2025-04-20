from src.widget import get_date, mask_account_card

# import pytest


def test_mask_account_card(test_data_widget):
    assert mask_account_card(test_data_widget[0]) == "Maestro 1596 83** **** 5199"

    assert mask_account_card(test_data_widget[1]) == "Счет **9589"

    assert mask_account_card(test_data_widget[2]) == "MasterCard 7158 30** **** 6758"

    assert mask_account_card(test_data_widget[5]) == "Visa Platinum 8990 92** **** 5229"

    assert mask_account_card(test_data_widget[8]) == "Не удалось опознать"

    assert mask_account_card(test_data_widget[9]) == "Не удалось опознать"

    assert mask_account_card(test_data_widget[10]) == "Ошибка ввода"


def test_get_date():
    assert get_date("2018-06-30T02:08:58.425572") == "30.06.2018"

    assert get_date("2018-06-30") == "30.06.2018"

    assert get_date("30-06-2018T02:08:58.425572") == "Ошибка: неверный формат данных"

    assert get_date("") == "Ошибка: неверный формат данных"

    assert get_date(" ") == "Ошибка: неверный формат данных"

    assert get_date("3000-13-00") == "Ошибка: на данный момент, в году всего 12 месяцев"

    assert get_date("3000-00-32") == "Ошибка: на данный момент, в месяце не может быть больше 31 дня"
