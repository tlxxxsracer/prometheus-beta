import pytest
from datetime import datetime
from src.date_utils import add_days_to_date

def test_add_days_to_date_string_input():
    """Test adding days to a date given as a string."""
    assert add_days_to_date('2023-01-01', 5) == '2023-01-06'
    assert add_days_to_date('2023-12-31', 1) == '2024-01-01'

def test_add_days_to_date_datetime_input():
    """Test adding days to a date given as a datetime object."""
    date = datetime(2023, 1, 1)
    assert add_days_to_date(date, 5) == '2023-01-06'

def test_subtract_days():
    """Test subtracting days."""
    assert add_days_to_date('2023-01-15', -10) == '2023-01-05'

def test_multiple_years():
    """Test adding days across multiple years."""
    assert add_days_to_date('2022-12-31', 1) == '2023-01-01'
    assert add_days_to_date('2020-02-28', 1) == '2020-02-29'  # Leap year

def test_invalid_date_format():
    """Test that invalid date formats raise ValueError."""
    with pytest.raises(ValueError, match="Date must be in 'YYYY-MM-DD' format"):
        add_days_to_date('01-01-2023', 5)

def test_invalid_date_type():
    """Test that invalid date types raise TypeError."""
    with pytest.raises(TypeError, match="Date must be a string or datetime object"):
        add_days_to_date(12345, 5)

def test_invalid_days_type():
    """Test that invalid days type raises TypeError."""
    with pytest.raises(TypeError, match="Days must be an integer"):
        add_days_to_date('2023-01-01', '5')