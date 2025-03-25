from typing import List, TypeVar, Any

T = TypeVar('T')

def cartesian_tree_sort(arr: List[T]) -> List[T]:
    """
    Perform sorting using a custom Cartesian Tree Sort algorithm.
    
    This implementation uses a Cartesian Tree's properties to sort:
    1. Find the minimum element
    2. Recursively sort the remaining elements
    
    :param arr: Input list to be sorted
    :return: Sorted list
    :raises TypeError: If input is not a list
    :raises ValueError: If input list is empty
    """
    # Input validation
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    if not arr:
        raise ValueError("Input list cannot be empty")
    
    # Handle single element case
    if len(arr) <= 1:
        return arr.copy()
    
    # Create a copy to avoid modifying original
    working_list = arr.copy()
    
    # Find index of minimum element to use as pivot
    min_index = 0
    for i in range(1, len(working_list)):
        if working_list[i] < working_list[min_index]:
            min_index = i
    
    # Swap minimum to the front
    working_list[0], working_list[min_index] = working_list[min_index], working_list[0]
    
    # Recursive divide and conquer
    left = working_list[1:min_index+1]
    right = working_list[min_index+1:]
    
    # Recursively sort left and right
    sorted_left = cartesian_tree_sort(left)
    sorted_right = cartesian_tree_sort(right)
    
    # Combine: First element (minimum) + left + right
    return [working_list[0]] + sorted_left + sorted_right