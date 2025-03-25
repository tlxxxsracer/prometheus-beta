import pytest
from src.max_subarray_product_sum import find_max_subarray_product_sum

def test_basic_case():
    """Test a basic scenario with a valid subarray."""
    arr = [1, 2, 3, 4]
    target_product = 6
    assert find_max_subarray_product_sum(arr, target_product) == 5  # 2 + 3

def test_single_element_match():
    """Test when a single element matches the target product."""
    arr = [1, 2, 3, 4]
    target_product = 3
    assert find_max_subarray_product_sum(arr, target_product) == 3

def test_multiple_valid_subarrays():
    """Test when multiple subarrays match the target product."""
    arr = [1, 2, 3, 2, 4]
    target_product = 6
    assert find_max_subarray_product_sum(arr, target_product) == 9  # 3 + 2 + 4

def test_no_matching_subarray():
    """Test when no subarray matches the target product."""
    arr = [1, 2, 3, 4]
    target_product = 100
    assert find_max_subarray_product_sum(arr, target_product) == -1

def test_empty_array_raises_error():
    """Test that an empty array raises a ValueError."""
    with pytest.raises(ValueError, match="Input array cannot be empty"):
        find_max_subarray_product_sum([], 10)

def test_non_positive_integers_raises_error():
    """Test that an array with non-positive integers raises a ValueError."""
    with pytest.raises(ValueError, match="All array elements must be positive integers"):
        find_max_subarray_product_sum([1, 2, -3, 4], 10)

def test_large_numbers():
    """Test with larger numbers."""
    arr = [10, 20, 30, 40, 50]
    target_product = 600
    assert find_max_subarray_product_sum(arr, target_product) == 90  # 30 + 40 + 20

def test_exact_target_in_middle():
    """Test when the exact product is found in the middle of array."""
    arr = [1, 2, 3, 4, 5, 6]
    target_product = 24  # 2 * 3 * 4
    assert find_max_subarray_product_sum(arr, target_product) == 9  # 2 + 3 + 4