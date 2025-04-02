def library_sort(arr):
    """
    Implement the Library Sort (Adaptive Sorting) algorithm.
    
    Library Sort is an adaptive sorting algorithm that works by creating 
    a series of "shelves" with gaps to allow for efficient insertion.
    
    Args:
        arr (list): The input list to be sorted.
    
    Returns:
        list: A sorted version of the input list.
    
    Raises:
        TypeError: If the input is not a list or contains non-comparable elements.
    """
    # Handle edge cases
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    if len(arr) <= 1:
        return arr.copy()
    
    # Initial parameters
    epsilon = 1  # Gap factor
    sorted_arr = [None] * (len(arr) + 1)  # Create a list with extra space
    
    # Insert first element
    sorted_arr[0] = arr[0]
    inserted_count = 1
    
    # Insert remaining elements
    for item in arr[1:]:
        # Find insertion point
        insertion_index = 0
        while insertion_index < inserted_count and sorted_arr[insertion_index] is not None:
            if item < sorted_arr[insertion_index]:
                break
            insertion_index += 1
        
        # Shift elements to make space
        if insertion_index < inserted_count:
            # Shift elements to the right
            for j in range(inserted_count, insertion_index, -1):
                sorted_arr[j] = sorted_arr[j-1]
        
        # Insert the item
        sorted_arr[insertion_index] = item
        inserted_count += 1
    
    # Remove None values and return
    return [x for x in sorted_arr if x is not None]