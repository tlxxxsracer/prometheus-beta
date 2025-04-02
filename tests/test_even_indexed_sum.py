import pytest
from src.even_indexed_sum import sum_even_indexed_elements

def test_even_indexed_sum_normal_list():
    """Test sum of even-indexed elements in a normal list."""
    assert sum_even_indexed_elements([1, 2, 3, 4, 5]) == 9

def test_even_indexed_sum_negative_numbers():
    """Test sum with negative numbers."""
    assert sum_even_indexed_elements([-1, 2, -3, 4, -5]) == -9

def test_even_indexed_sum_empty_list():
    """Test sum with an empty list."""
    assert sum_even_indexed_elements([]) == 0

def test_even_indexed_sum_single_element():
    """Test sum with a single element list."""
    assert sum_even_indexed_elements([42]) == 42

def test_even_indexed_sum_mixed_numbers():
    """Test sum with mixed positive and negative numbers."""
    assert sum_even_indexed_elements([-10, 5, 15, -7, 20]) == 25

def test_even_indexed_sum_zero_values():
    """Test sum with zero values."""
    assert sum_even_indexed_elements([0, 1, 0, 2, 0]) == 0