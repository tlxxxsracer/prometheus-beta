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
    min_index = working_list.index(min(working_list))
    
    # If minimum is not at the start, perform partition
    if min_index > 0:
        # Rotate the list so minimum is first
        working_list = [
            working_list[min_index]
        ] + working_list[:min_index] + working_list[min_index+1:]
    
    # If list has more than one element after minimum
    if len(working_list) > 1:
        # Recursively sort the rest of the list
        rest_sorted = cartesian_tree_sort(working_list[1:])
        return [working_list[0]] + rest_sorted
    
    return working_list