import pytest
from src.longest_increasing_subsequence import find_longest_increasing_subsequence

def test_basic_increasing_sequence():
    arr = [10, 22, 33, 44, 55]
    result = find_longest_increasing_subsequence(arr)
    assert result == arr

def test_mixed_sequence():
    arr = [10, 22, 9, 33, 21, 50, 41, 60]
    result = find_longest_increasing_subsequence(arr)
    assert result == [10, 22, 33, 50, 60]

def test_empty_sequence():
    arr = []
    result = find_longest_increasing_subsequence(arr)
    assert result == []

def test_duplicate_elements():
    arr = [1, 2, 2, 3, 1, 4]
    result = find_longest_increasing_subsequence(arr)
    assert result == [1, 2, 3, 4]

def test_single_element():
    arr = [5]
    result = find_longest_increasing_subsequence(arr)
    assert result == [5]

def test_descending_sequence():
    arr = [5, 4, 3, 2, 1]
    result = find_longest_increasing_subsequence(arr)
    assert result == [5] or result == [4] or result == [3] or result == [2] or result == [1]

def test_invalid_input_raises_type_error():
    with pytest.raises(TypeError):
        find_longest_increasing_subsequence("not a list")

def test_non_comparable_elements_raise_value_error():
    with pytest.raises(ValueError):
        find_longest_increasing_subsequence([1, 2, None, 3, 4])

def test_negative_elements():
    arr = [-5, -4, -3, -2, -1]
    result = find_longest_increasing_subsequence(arr)
    assert result == [-5, -4, -3, -2, -1]

def test_complex_mixed_sequence():
    arr = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
    result = find_longest_increasing_subsequence(arr)
    # Verify the result is a valid LIS
    assert len(result) == 6
    assert all(result[i] < result[i+1] for i in range(len(result)-1))
    assert all(x in arr for x in result)