import pytest
from src.merge_sort import merge_sort

def test_merge_sort_basic():
    """Test basic sorting of integers"""
    assert merge_sort([4, 2, 7, 1, 5, 3]) == [1, 2, 3, 4, 5, 7]

def test_merge_sort_already_sorted():
    """Test sorting an already sorted list"""
    assert merge_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_merge_sort_reverse_sorted():
    """Test sorting a reverse sorted list"""
    assert merge_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_merge_sort_duplicates():
    """Test sorting a list with duplicate elements"""
    assert merge_sort([3, 1, 4, 1, 5, 9, 2, 6, 5]) == [1, 1, 2, 3, 4, 5, 5, 6, 9]

def test_merge_sort_empty_list():
    """Test sorting an empty list"""
    assert merge_sort([]) == []

def test_merge_sort_single_element():
    """Test sorting a list with a single element"""
    assert merge_sort([42]) == [42]

def test_merge_sort_with_floats():
    """Test sorting a list of floats"""
    assert merge_sort([3.14, 2.71, 1.41, 0.58]) == [0.58, 1.41, 2.71, 3.14]

def test_merge_sort_preserves_original():
    """Ensure the original list is not modified"""
    original = [4, 2, 7, 1, 5, 3]
    merge_sort(original)
    assert original == [4, 2, 7, 1, 5, 3]

def test_merge_sort_type_error():
    """Test that a TypeError is raised for non-list inputs"""
    with pytest.raises(TypeError, match="Input must be a list"):
        merge_sort("not a list")
        merge_sort(123)
        merge_sort(None)

def test_merge_sort_with_strings():
    """Test sorting a list of strings"""
    assert merge_sort(["banana", "apple", "cherry"]) == ["apple", "banana", "cherry"]