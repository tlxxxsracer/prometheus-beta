import pytest
from src.max_consecutive_product import find_max_consecutive_product

def test_positive_numbers():
    """Test with an array of positive numbers."""
    arr = [1, 2, 3, 4, 5]
    assert find_max_consecutive_product(arr) == 60

def test_negative_numbers():
    """Test with an array containing negative numbers."""
    arr = [-1, -2, -3, 1, 2, 3]
    assert find_max_consecutive_product(arr) == 6

def test_mixed_numbers():
    """Test with an array of mixed positive and negative numbers."""
    arr = [-10, 5, 2, 4, -8, 3]
    assert find_max_consecutive_product(arr) == 40

def test_with_zero():
    """Test an array that includes zero."""
    arr = [1, 0, 2, 3, 4]
    assert find_max_consecutive_product(arr) == 0

def test_minimum_length():
    """Test the minimum length array."""
    arr = [1, 2, 3]
    assert find_max_consecutive_product(arr) == 6

def test_large_numbers():
    """Test with large numbers."""
    arr = [1000, 100, 10, 1]
    assert find_max_consecutive_product(arr) == 1000000

def test_error_too_few_elements():
    """Test error handling when array is too short."""
    with pytest.raises(ValueError):
        find_max_consecutive_product([1, 2])

def test_error_empty_array():
    """Test error handling with an empty array."""
    with pytest.raises(ValueError):
        find_max_consecutive_product([])