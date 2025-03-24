import pytest
from src.bitwise_and_range import bitwise_and_range

def test_bitwise_and_range_basic():
    """Test basic bitwise AND range calculations."""
    assert bitwise_and_range(5, 7) == 4
    assert bitwise_and_range(0, 1) == 0
    assert bitwise_and_range(10, 10) == 10

def test_bitwise_and_range_large_numbers():
    """Test bitwise AND range with larger numbers."""
    assert bitwise_and_range(100, 200) == 0
    assert bitwise_and_range(1024, 2048) == 0

def test_bitwise_and_range_identical_numbers():
    """Test when lower and upper bounds are the same."""
    assert bitwise_and_range(42, 42) == 42
    assert bitwise_and_range(0, 0) == 0

def test_bitwise_and_range_power_of_two():
    """Test ranges involving powers of two."""
    assert bitwise_and_range(8, 15) == 8
    assert bitwise_and_range(16, 31) == 16

def test_bitwise_and_range_error_handling():
    """Test error handling for invalid inputs."""
    with pytest.raises(ValueError, match="Inputs must be non-negative integers"):
        bitwise_and_range(-1, 10)
    
    with pytest.raises(ValueError, match="Inputs must be non-negative integers"):
        bitwise_and_range(10, -1)
    
    with pytest.raises(ValueError, match="Lower bound must not be greater than upper bound"):
        bitwise_and_range(10, 5)

def test_bitwise_and_range_zero_range():
    """Test bitwise AND range with zero-oriented ranges."""
    assert bitwise_and_range(0, 5) == 0
    assert bitwise_and_range(0, 0) == 0