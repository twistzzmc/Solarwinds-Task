import pytest
from source.main import main


def test_bad_columns():
    with pytest.raises(ValueError) as ve:
        main('tests/test_files/bad_columns.csv')


def test_bad_date():
    with pytest.raises(ValueError):
        main('tests/test_files/bad_date.csv')


def test_bad_date_order():
    with pytest.raises(ValueError):
        main('tests/test_files/bad_date_order.csv')


def test_bad_event():
    with pytest.raises(ValueError):
        main('tests/test_files/bad_event.csv')
