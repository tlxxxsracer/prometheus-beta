import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from bucket_sort import bucket_sort

def test_basic_sorting():
    """Test basic functionality with a simple list of numbers."""
    input_list = [0.5, 0.3, 0.9, 0.1, 0.7]
    result = bucket_sort(input_list)
    assert result == sorted(input_list)

def test_integer_sorting():
    """Test sorting with integer values."""
    input_list = [64, 34, 25, 12, 22, 11, 90]
    result = bucket_sort(input_list)
    assert result == sorted(input_list)

def test_already_sorted():
    """Test sorting an already sorted list."""
    input_list = [1, 2, 3, 4, 5]
    result = bucket_sort(input_list)
    assert result == input_list

def test_reverse_sorted():
    """Test sorting a reverse-sorted list."""
    input_list = [5, 4, 3, 2, 1]
    result = bucket_sort(input_list)
    assert result == sorted(input_list)

def test_with_duplicates():
    """Test sorting a list with duplicate values."""
    input_list = [5, 2, 9, 1, 5, 6, 2]
    result = bucket_sort(input_list)
    assert result == sorted(input_list)

def test_negative_numbers():
    """Test sorting with negative numbers."""
    input_list = [-5, 2, -9, 1, 0, -3, 6]
    result = bucket_sort(input_list)
    assert result == sorted(input_list)

def test_mixed_numbers():
    """Test sorting with mixed positive and negative floating point numbers."""
    input_list = [-3.5, 2.1, 0.0, -1.2, 5.7]
    result = bucket_sort(input_list)
    assert result == sorted(input_list)

def test_custom_bucket_count():
    """Test sorting with a custom number of buckets."""
    input_list = [0.5, 0.3, 0.9, 0.1, 0.7]
    result = bucket_sort(input_list, num_buckets=3)
    assert result == sorted(input_list)

def test_single_element():
    """Test sorting a single-element list."""
    input_list = [42]
    result = bucket_sort(input_list)
    assert result == input_list

def test_error_empty_list():
    """Test error handling for empty list."""
    with pytest.raises(ValueError, match="Input list cannot be empty"):
        bucket_sort([])

def test_error_non_list_input():
    """Test error handling for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list"):
        bucket_sort("not a list")

def test_error_non_numeric_input():
    """Test error handling for non-numeric elements."""
    with pytest.raises(TypeError, match="All elements must be numeric"):
        bucket_sort([1, 2, "3", 4])