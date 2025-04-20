import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.mark.parametrize(
    "state, expected",
    [
        (
            "EXECUTED",
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
        (
            "",
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
        (
            "CANCELED",
            [
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
        ),
    ],
)
def test_filter_by_state(test_data_processing, state, expected):
    assert filter_by_state(test_data_processing, state) == expected


def test_sort_by_date_reversed(test_data_processing, sorted_by_test_data_reversed):
    assert sort_by_date(test_data_processing, True) == sorted_by_test_data_reversed

    assert sort_by_date(test_data_processing) == sorted_by_test_data_reversed


def test_sort_by_date(test_data_processing, sorted_by_test_data):
    assert sort_by_date(test_data_processing, False) == sorted_by_test_data
