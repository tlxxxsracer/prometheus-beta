import pytest
from src.library_sort import library_sort

def test_library_sort_basic():
    """Test basic sorting functionality."""
    assert library_sort([3, 1, 4, 1, 5, 9, 2, 6]) == [1, 1, 2, 3, 4, 5, 6, 9]

def test_library_sort_empty_list():
    """Test sorting an empty list."""
    assert library_sort([]) == []

def test_library_sort_single_element():
    """Test sorting a list with a single element."""
    assert library_sort([42]) == [42]

def test_library_sort_already_sorted():
    """Test sorting an already sorted list."""
    assert library_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_library_sort_reverse_sorted():
    """Test sorting a reverse-sorted list."""
    assert library_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_library_sort_duplicate_elements():
    """Test sorting a list with duplicate elements."""
    assert library_sort([3, 3, 3, 1, 1, 2]) == [1, 1, 2, 3, 3, 3]

def test_library_sort_negative_numbers():
    """Test sorting a list with negative numbers."""
    assert library_sort([-1, -5, 3, 0, 2]) == [-5, -1, 0, 2, 3]

def test_library_sort_mixed_types_comparable():
    """Test sorting comparable mixed types."""
    assert library_sort([3.14, 2.71, -1, 0]) == [-1, 0, 2.71, 3.14]

def test_library_sort_invalid_input():
    """Test that an invalid input raises a TypeError."""
    with pytest.raises(TypeError):
        library_sort("not a list")
    with pytest.raises(TypeError):
        library_sort(None)