import pytest
from src.array_intersection import find_array_intersection

def test_basic_intersection():
    """Test basic intersection of two arrays"""
    arr1 = [1, 2, 3, 4, 5]
    arr2 = [4, 5, 6, 7, 8]
    assert find_array_intersection(arr1, arr2) == [4, 5]

def test_no_intersection():
    """Test arrays with no common elements"""
    arr1 = [1, 2, 3]
    arr2 = [4, 5, 6]
    assert find_array_intersection(arr1, arr2) == []

def test_complete_intersection():
    """Test when all elements are common"""
    arr1 = [1, 2, 3]
    arr2 = [3, 2, 1]
    assert find_array_intersection(arr1, arr2) == [1, 2, 3]

def test_repeated_elements():
    """Test arrays with repeated elements"""
    arr1 = [1, 2, 2, 3, 4, 4, 5]
    arr2 = [2, 4, 4, 6, 7]
    assert find_array_intersection(arr1, arr2) == [2, 4]

def test_empty_arrays():
    """Test intersection with empty arrays"""
    arr1 = []
    arr2 = [1, 2, 3]
    assert find_array_intersection(arr1, arr2) == []
    assert find_array_intersection(arr2, arr1) == []

def test_invalid_input_type():
    """Test error handling for non-list inputs"""
    with pytest.raises(TypeError):
        find_array_intersection(123, [1, 2, 3])
    with pytest.raises(TypeError):
        find_array_intersection([1, 2, 3], "string")

def test_invalid_element_type():
    """Test error handling for non-integer elements"""
    with pytest.raises(ValueError):
        find_array_intersection([1, 2, 'a'], [3, 4, 5])
    with pytest.raises(ValueError):
        find_array_intersection([1, 2, 3], [4, 5, '6'])