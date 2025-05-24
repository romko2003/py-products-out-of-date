import datetime
import pytest
from unittest.mock import patch
from app.main import outdated_products  # імпортуй правильно, якщо структура інша — поправ

REAL_DATE = datetime.date  # Зберігаємо справжній datetime.date

@patch("datetime.date")
def test_outdated_products_some_expired(mock_date):
    mock_date.today.return_value = REAL_DATE(2022, 2, 2)
    mock_date.side_effect = lambda *args, **kwargs: REAL_DATE(*args, **kwargs)

    products = [
        {"name": "salmon", "expiration_date": REAL_DATE(2022, 2, 10), "price": 600},
        {"name": "chicken", "expiration_date": REAL_DATE(2022, 2, 5), "price": 120},
        {"name": "duck", "expiration_date": REAL_DATE(2022, 2, 1), "price": 160},
    ]
    assert outdated_products(products) == ["duck"]


@patch("datetime.date")
def test_outdated_products_all_fresh(mock_date):
    mock_date.today.return_value = REAL_DATE(2022, 2, 1)
    mock_date.side_effect = lambda *args, **kwargs: REAL_DATE(*args, **kwargs)

    products = [
        {"name": "salmon", "expiration_date": REAL_DATE(2022, 2, 10), "price": 600},
        {"name": "chicken", "expiration_date": REAL_DATE(2022, 2, 5), "price": 120},
    ]
    assert outdated_products(products) == []


@patch("datetime.date")
def test_outdated_products_all_expired(mock_date):
    mock_date.today.return_value = REAL_DATE(2022, 2, 20)
    mock_date.side_effect = lambda *args, **kwargs: REAL_DATE(*args, **kwargs)

    products = [
        {"name": "old cheese", "expiration_date": REAL_DATE(2022, 1, 15), "price": 70},
        {"name": "yogurt", "expiration_date": REAL_DATE(2022, 2, 1), "price": 25},
    ]
    assert outdated_products(products) == ["old cheese", "yogurt"]


@patch("datetime.date")
def test_outdated_products_empty_list(mock_date):
    mock_date.today.return_value = REAL_DATE(2022, 2, 2)
    mock_date.side_effect = lambda *args, **kwargs: REAL_DATE(*args, **kwargs)

    assert outdated_products([]) == []
