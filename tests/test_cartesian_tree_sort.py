import pytest
from src.cartesian_tree_sort import cartesian_tree_sort, build_cartesian_tree, CartesianTreeNode

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

def test_mixed_type_list():
    """Test a list with mixed types of elements that can be sorted."""
    input_list = [5, 'a', 3, 'b', 1, 'c']
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

def test_build_cartesian_tree():
    """Test the Cartesian Tree construction."""
    input_list = [9, 3, 7, 1, 8, 12, 10, 20, 15]
    root = build_cartesian_tree(input_list)
    
    # Verify root value
    assert root.value == 9
    
    # Test tree structure (simplified)
    assert root.left.value == 3
    assert root.right.value == 12