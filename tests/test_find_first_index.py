import pytest
from src.find_first_index import find_first_index

def test_find_first_index_basic():
    """Test basic functionality of finding an existing value."""
    assert find_first_index([1, 2, 3, 4, 2], 2) == 1
    assert find_first_index([5, 5, 5, 5], 5) == 0

def test_find_first_index_not_found():
    """Test when the target value is not in the list."""
    assert find_first_index([1, 2, 3, 4, 5], 6) == -1

def test_find_first_index_empty_list():
    """Test behavior with an empty list."""
    assert find_first_index([], 1) == -1

def test_find_first_index_multiple_occurrences():
    """Test that the first occurrence is returned when target appears multiple times."""
    assert find_first_index([1, 2, 3, 2, 4], 2) == 1

def test_find_first_index_first_element():
    """Test finding target at the first element."""
    assert find_first_index([5, 1, 2, 3], 5) == 0

def test_find_first_index_last_element():
    """Test finding target at the last element."""
    assert find_first_index([1, 2, 3, 4, 5], 5) == 4

def test_find_first_index_type_handling():
    """Verify the function works with various integer types."""
    assert find_first_index([1, 2, 3, 4], 2) == 1
    assert find_first_index([-1, -2, 0, 1], -2) == 1