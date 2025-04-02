import pytest
from src.two_sum import two_sum

def test_two_sum_basic():
    """Test basic two sum scenario"""
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]

def test_two_sum_multiple_solutions():
    """Ensure first valid solution is returned"""
    assert two_sum([3, 2, 4], 6) == [1, 2]

def test_two_sum_no_solution():
    """Test when no solution exists"""
    assert two_sum([1, 2, 3, 4], 10) == []

def test_two_sum_repeated_numbers():
    """Test with repeated numbers"""
    assert two_sum([3, 3], 6) == [0, 1]

def test_two_sum_invalid_input_not_list():
    """Test invalid input type"""
    with pytest.raises(TypeError, match="Input must be a list"):
        two_sum("not a list", 10)

def test_two_sum_invalid_target_type():
    """Test invalid target type"""
    with pytest.raises(TypeError, match="Target must be an integer"):
        two_sum([1, 2, 3], "10")

def test_two_sum_non_integer_elements():
    """Test list with non-integer elements"""
    with pytest.raises(ValueError, match="All list elements must be integers"):
        two_sum([1, 2, "3"], 6)

def test_two_sum_empty_list():
    """Test with an empty list"""
    assert two_sum([], 10) == []

def test_two_sum_large_numbers():
    """Test with large numbers"""
    assert two_sum([1000000, 1000001, 1], 1000001) == [0, 1]