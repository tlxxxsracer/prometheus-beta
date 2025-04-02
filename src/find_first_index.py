def find_first_index(nums: list[int], target: int) -> int:
    """
    Find the index of the first occurrence of a target value in a list of integers.

    Args:
        nums (list[int]): The input list of integers to search through.
        target (int): The value to find in the list.

    Returns:
        int: The index of the first occurrence of the target value,
             or -1 if the target is not found in the list.

    Examples:
        >>> find_first_index([1, 2, 3, 4, 2], 2)
        1
        >>> find_first_index([1, 2, 3, 4, 5], 6)
        -1
        >>> find_first_index([], 1)
        -1
    """
    # Iterate through the list with enumeration to get both index and value
    for index, value in enumerate(nums):
        if value == target:
            return index
    
    # Return -1 if the target is not found
    return -1