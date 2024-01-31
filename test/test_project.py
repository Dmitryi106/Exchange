import pytest

from func import new_list, sorted_list, format_operation

def test_new_list():
    assert new_list([
        {"id": 1, "state": "EXECUTED"},
        {"id": 2, "state": "CANCELED"},
        {"id": 3, "state": "FAILED"}
    ]) == [{"id": 1, "state": "EXECUTED"}]

def test_sorted_list():
    assert sorted_list([
        {"id": 1, "date": "2020-01-01"},
        {"id": 2, "date": "2019-12-31"},
        {"id": 3, "date": "2020-02-29"}
    ]) == [
        {"id": 3, "date": "2020-02-29"},
        {"id": 1, "date": "2020-01-01"},
        {"id": 2, "date": "2019-12-31"}
    ]

def test_format_operation():
    assert format_operation({
        "date": "2020-01-01T10:30:00.000000",
        "operationAmount": {"amount": "100.00", "currency": {"name": "USD"}},
        "description": "Test Operation",
        "from": "Счет 74489636417521191160",
        "to": "Счет 53489636427521156732"
    }) == "01.01.2020 Test Operation\nСчет **1160 -> Счет **6732\n100.00 USD"
