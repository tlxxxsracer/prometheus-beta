def counting_sort(arr):
    """
    Implement Counting Sort algorithm for sorting a list of non-negative integers.
    
    Args:
        arr (list): A list of non-negative integers to be sorted.
    
    Returns:
        list: A sorted version of the input list.
    
    Raises:
        ValueError: If the input contains negative numbers.
        TypeError: If the input is not a list or contains non-integer elements.
    """
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Handle empty list
    if not arr:
        return []
    
    # Check for non-integer elements or negative numbers
    for item in arr:
        if not isinstance(item, int):
            raise TypeError("All elements must be integers")
        if item < 0:
            raise ValueError("Counting sort only works with non-negative integers")
    
    # Find the range of the input
    max_val = max(arr)
    
    # Create counting array and initialize with zeros
    count = [0] * (max_val + 1)
    
    # Count occurrences of each unique object
    for num in arr:
        count[num] += 1
    
    # Modify the count array to store actual position of each object
    for i in range(1, len(count)):
        count[i] += count[i-1]
    
    # Create output array
    output = [0] * len(arr)
    
    # Build the output array
    for i in range(len(arr) - 1, -1, -1):
        output[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1
    
    return output