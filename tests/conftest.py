import pytest


# для test_masks.py
@pytest.fixture
def correct_form_card_number():
    return "0000 00** **** 0000"


# для test_masks.py
@pytest.fixture
def correct_form_account_number():
    return "**0000"


# для test_masks.py
@pytest.fixture
def input_error():
    return "Ошибка ввода"


# для test_masks.py
# список вариантов для номера карты, который используется для сценария ввода неверных значений
@pytest.fixture
def card_number_variations():
    return [
        "",
        " ",
        "                ",
        "0000 0000 0000",
        "0000 0000 0000 0000 0000",
        "0000-0000-0000-0000",
        "AAAAAAAAAAAAAAAA",
        "AAAA AAAA AAAA AAAA",
        "AAAA-AAAA-AAAA-AAAA",
    ]


# для test_masks.py
# список вариантов для номера аккаунта, который используется для сценария ввода неверных значений
@pytest.fixture
def account_number_variations():
    return [
        "",
        " ",
        "                ",
        "0000 0000 0000 0000",
        "0000 0000 0000 0000 0000 0000",
        "0000-0000-0000-0000-0000",
        "AAAAAAAAAAAAAAAAAAAA",
        "AAAA AAAA AAAA AAAA AAAA",
        "AAAA-AAAA-AAAA-AAAA-AAAA",
    ]


# для test_processing.py
@pytest.fixture
def test_data_processing():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


# для test_processing.py
@pytest.fixture
def sorted_by_test_data():
    return [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]


# для test_processing.py
@pytest.fixture
def sorted_by_test_data_reversed():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


# для test_widget.py
@pytest.fixture
def test_data_widget():
    return [
        "Maestro 1596837868705199",
        "Счет 64686473678894779589",
        "MasterCard 7158300734726758",
        "Счет 35383033474447895560",
        "Visa Classic 6831982476737658",
        "Visa Platinum 8990922113665229",
        "Visa Gold 5999414228426353",
        "Счет 73654108430135874305",
        "Mastermind 0000000000000000",
        "Visa Diamond 1596837868705199",
        "Visa Classic 00000000000000000000",
    ]
