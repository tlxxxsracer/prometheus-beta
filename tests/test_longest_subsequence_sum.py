import pytest
from src.longest_subsequence_sum import longest_subsequence_with_target_sum

def test_basic_subsequence():
    """Test a basic scenario with a single valid subsequence"""
    arr = [1, 2, 3, 4, 5]
    target = 9
    assert longest_subsequence_with_target_sum(arr, target) == 2

def test_multiple_subsequences():
    """Test a scenario with multiple possible subsequences"""
    arr = [1, 1, 1, 2, 3, 4, 5]
    target = 5
    assert longest_subsequence_with_target_sum(arr, target) == 3

def test_empty_array():
    """Test handling of an empty array"""
    arr = []
    target = 10
    assert longest_subsequence_with_target_sum(arr, target) == 0

def test_no_valid_subsequence():
    """Test case where no subsequence matches the target"""
    arr = [1, 2, 3, 4, 5]
    target = 100
    assert longest_subsequence_with_target_sum(arr, target) == 0

def test_single_element_match():
    """Test scenario with a single element matching the target"""
    arr = [1, 5, 2, 3, 7]
    target = 5
    assert longest_subsequence_with_target_sum(arr, target) == 1

def test_full_array_match():
    """Test scenario where entire array matches the target"""
    arr = [1, 2, 3, 4]
    target = 10
    assert longest_subsequence_with_target_sum(arr, target) == 4

def test_repeated_elements():
    """Test array with repeated elements"""
    arr = [1, 1, 1, 1, 1]
    target = 3
    assert longest_subsequence_with_target_sum(arr, target) == 3

def test_negative_numbers():
    """Test array with negative numbers"""
    arr = [-1, 1, 2, -2, 3, -3]
    target = 2
    assert longest_subsequence_with_target_sum(arr, target) == 3

def test_large_numbers():
    """Test scenario with large numbers"""
    arr = [1000, 2000, 3000, 4000, 5000]
    target = 6000
    assert longest_subsequence_with_target_sum(arr, target) == 2

def test_zero_target():
    """Test case with zero as the target sum"""
    arr = [-1, 1, 0, 2, -2]
    target = 0
    assert longest_subsequence_with_target_sum(arr, target) == 3