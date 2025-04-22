import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency(test_data_generators, test_data_generators_usd, test_data_generators_rub):  # type: ignore
    result_usd = list(filter_by_currency(test_data_generators))
    result_rub = list(filter_by_currency(test_data_generators, "RUB"))
    result_not_found = list(filter_by_currency(test_data_generators, "GBP"))

    assert result_usd == test_data_generators_usd

    assert result_rub == test_data_generators_rub

    assert result_not_found == []


@pytest.mark.parametrize(
    "result_index, data_index",
    [
        (0, 0),
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
    ],
)
def test_transaction_descriptions(result_index, data_index, test_data_generators, test_data_generators_description):  # type: ignore
    result = list(transaction_descriptions(test_data_generators))

    assert result[result_index] == test_data_generators_description[data_index]


def test_card_number_generator(card_number_generator_first_ten, card_number_generator_last_ten):  # type: ignore
    result_first_ten = list(card_number_generator(0, 10))
    result_last_ten = list(card_number_generator(10**16 - 10, 10**16))

    assert result_first_ten == card_number_generator_first_ten

    assert result_last_ten == card_number_generator_last_ten
