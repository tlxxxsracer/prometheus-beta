import pytest
from src.temperature_converter import fahrenheit_to_celsius

def test_freezing_point():
    """Test conversion of freezing point of water."""
    assert fahrenheit_to_celsius(32) == 0

def test_boiling_point():
    """Test conversion of boiling point of water."""
    assert fahrenheit_to_celsius(212) == 100

def test_zero_fahrenheit():
    """Test conversion of 0°F."""
    assert fahrenheit_to_celsius(0) == -17.78

def test_negative_fahrenheit():
    """Test conversion of negative Fahrenheit temperature."""
    assert fahrenheit_to_celsius(-40) == -40

def test_decimal_fahrenheit():
    """Test conversion with decimal input."""
    assert fahrenheit_to_celsius(98.6) == 37

def test_type_error():
    """Test that TypeError is raised for non-numeric input."""
    with pytest.raises(TypeError, match="Input must be a number"):
        fahrenheit_to_celsius("not a number")
    with pytest.raises(TypeError, match="Input must be a number"):
        fahrenheit_to_celsius(None)
    with pytest.raises(TypeError, match="Input must be a number"):
        fahrenheit_to_celsius([32])