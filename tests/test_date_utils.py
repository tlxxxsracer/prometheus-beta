import pytest
from datetime import datetime, timedelta
from src.date_utils import add_days_to_date

def test_add_days_to_date_string_input():
    """Test adding days to a date string input"""
    result = add_days_to_date('2023-05-15', 10)
    assert result == datetime(2023, 5, 25)

def test_add_days_to_date_datetime_input():
    """Test adding days to a datetime input"""
    input_date = datetime(2023, 5, 15)
    result = add_days_to_date(input_date, 10)
    assert result == datetime(2023, 5, 25)

def test_subtract_days():
    """Test subtracting days with negative input"""
    result = add_days_to_date('2023-05-15', -5)
    assert result == datetime(2023, 5, 10)

def test_zero_days():
    """Test adding zero days"""
    result = add_days_to_date('2023-05-15', 0)
    assert result == datetime(2023, 5, 15)

def test_leap_year():
    """Test adding days across a leap year"""
    result = add_days_to_date('2024-02-28', 1)
    assert result == datetime(2024, 2, 29)

def test_invalid_date_string():
    """Test invalid date string format"""
    with pytest.raises(ValueError, match="Input date must be in 'YYYY-MM-DD' format"):
        add_days_to_date('15-05-2023', 10)

def test_invalid_days_type():
    """Test invalid type for days_to_add"""
    with pytest.raises(TypeError, match="days_to_add must be an integer"):
        add_days_to_date('2023-05-15', '10')

def test_invalid_input_date_type():
    """Test invalid input date type"""
    with pytest.raises(TypeError, match="input_date must be a datetime object or a date string"):
        add_days_to_date(12345, 10)