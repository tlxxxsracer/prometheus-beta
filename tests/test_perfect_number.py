import pytest
from src.perfect_number import is_perfect_number

def test_known_perfect_numbers():
    """Test known perfect numbers."""
    perfect_numbers = [6, 28, 496, 8128]
    for num in perfect_numbers:
        assert is_perfect_number(num), f"{num} should be a perfect number"

def test_non_perfect_numbers():
    """Test some numbers that are not perfect numbers."""
    non_perfect_numbers = [5, 10, 100, 1000]
    for num in non_perfect_numbers:
        assert not is_perfect_number(num), f"{num} should not be a perfect number"

def test_edge_cases():
    """Test edge cases and boundary conditions."""
    # Test 0 and negative numbers
    assert not is_perfect_number(0), "0 should not be a perfect number"
    assert not is_perfect_number(-6), "Negative numbers should not be perfect numbers"
    assert not is_perfect_number(1), "1 should not be a perfect number"

def test_input_validation():
    """Test input validation."""
    with pytest.raises(ValueError, match="Input must be an integer"):
        is_perfect_number(6.5)
    
    with pytest.raises(ValueError, match="Input must be an integer"):
        is_perfect_number("6")
    
    with pytest.raises(ValueError, match="Input must be an integer"):
        is_perfect_number(None)