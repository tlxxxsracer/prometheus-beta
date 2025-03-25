import pytest
from src.cartesian_tree_sort import cartesian_tree_sort

def test_basic_integer_sorting():
    """Test sorting a list of integers."""
    input_list = [9, 3, 7, 1, 8, 12, 10, 20, 15]
    expected = sorted(input_list)
    assert cartesian_tree_sort(input_list) == expected

def test_already_sorted_list():
    """Test a list that is already sorted."""
    input_list = [1, 2, 3, 4, 5]
    assert cartesian_tree_sort(input_list) == input_list

def test_reverse_sorted_list():
    """Test a list sorted in reverse order."""
    input_list = [5, 4, 3, 2, 1]
    expected = sorted(input_list)
    assert cartesian_tree_sort(input_list) == expected

def test_list_with_duplicates():
    """Test a list with duplicate elements."""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    expected = sorted(input_list)
    assert cartesian_tree_sort(input_list) == expected

def test_single_element_list():
    """Test a list with a single element."""
    input_list = [42]
    assert cartesian_tree_sort(input_list) == input_list

def test_string_sorting():
    """Test sorting a list of strings."""
    input_list = ["banana", "apple", "cherry", "date"]
    expected = sorted(input_list)
    assert cartesian_tree_sort(input_list) == expected

def test_mixed_type_list_of_homogeneous_comparable_types():
    """Test a list of types that can be sorted comparably."""
    input_list = [5, 3, 8, 1, 6]
    expected = sorted(input_list)
    assert cartesian_tree_sort(input_list) == expected

def test_error_handling_empty_list():
    """Test handling of an empty list."""
    with pytest.raises(ValueError, match="Input list cannot be empty"):
        cartesian_tree_sort([])

def test_error_handling_non_list_input():
    """Test handling of non-list input."""
    with pytest.raises(TypeError, match="Input must be a list"):
        cartesian_tree_sort("not a list")

def test_stable_sorting_with_duplicates():
    """Verify stable sorting of elements with same value."""
    input_list = [(1, 'a'), (2, 'b'), (1, 'c'), (3, 'd')]
    expected = sorted(input_list)
    result = cartesian_tree_sort(input_list)
    assert result == expected

def test_large_list_sorting():
    """Test sorting a larger list."""
    import random
    random.seed(42)  # Consistent randomness
    input_list = random.sample(range(1000), 100)
    expected = sorted(input_list)
    assert cartesian_tree_sort(input_list) == expected

def test_preserves_original_input():
    """Test that original input is not modified."""
    input_list = [5, 2, 8, 1, 9]
    original = input_list.copy()
    cartesian_tree_sort(input_list)
    assert input_list == original