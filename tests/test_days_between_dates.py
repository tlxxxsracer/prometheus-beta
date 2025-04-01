import pytest
from datetime import date, timedelta
from src.days_between_dates import calculate_days_between_dates

def test_same_date():
    """Test when both dates are the same"""
    assert calculate_days_between_dates("2023-01-01", "2023-01-01") == 0
    assert calculate_days_between_dates(date(2023, 1, 1), date(2023, 1, 1)) == 0

def test_adjacent_dates():
    """Test dates that are one day apart"""
    assert calculate_days_between_dates("2023-01-01", "2023-01-02") == 1
    assert calculate_days_between_dates(date(2023, 1, 1), date(2023, 1, 2)) == 1

def test_date_order_doesnt_matter():
    """Test that order of dates doesn't affect result"""
    assert calculate_days_between_dates("2023-01-01", "2023-01-10") == \
           calculate_days_between_dates("2023-01-10", "2023-01-01")

def test_date_across_year_boundary():
    """Test calculation of days across year boundary"""
    assert calculate_days_between_dates("2022-12-31", "2023-01-01") == 1

def test_leap_year():
    """Test calculation of days including a leap year"""
    assert calculate_days_between_dates("2020-02-28", "2020-03-01") == 2

def test_large_date_difference():
    """Test calculation of days with a large date difference"""
    assert calculate_days_between_dates("2000-01-01", "2023-01-01") == 8401

def test_invalid_date_format():
    """Test handling of invalid date formats"""
    with pytest.raises(ValueError, match="Invalid date format"):
        calculate_days_between_dates("2023/01/01", "2023-01-02")
    
    with pytest.raises(ValueError, match="Invalid date format"):
        calculate_days_between_dates("01-01-2023", "2023-01-02")

def test_invalid_input_type():
    """Test handling of invalid input types"""
    with pytest.raises(ValueError, match="Dates must be"):
        calculate_days_between_dates(123, "2023-01-02")
    
    with pytest.raises(ValueError, match="Dates must be"):
        calculate_days_between_dates(None, date(2023, 1, 1))