def bucket_sort(arr, num_buckets=None):
    """
    Implement the bucket sort algorithm.
    
    Args:
        arr (list): The input list of numbers to be sorted.
        num_buckets (int, optional): Number of buckets to use. 
                                     If None, defaults to len(arr).
    
    Returns:
        list: A sorted version of the input list.
    
    Raises:
        TypeError: If input is not a list or contains non-numeric elements.
        ValueError: If input list is empty.
    """
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    if len(arr) == 0:
        raise ValueError("Input list cannot be empty")
    
    # Check for non-numeric elements
    if not all(isinstance(x, (int, float)) for x in arr):
        raise TypeError("All elements must be numeric")
    
    # Determine number of buckets
    if num_buckets is None:
        num_buckets = len(arr)
    
    # Handle single element or empty list cases
    if len(arr) <= 1:
        return arr.copy()
    
    # Find min and max values
    min_val = min(arr)
    max_val = max(arr)
    
    # Handle case where all elements are the same
    if min_val == max_val:
        return arr.copy()
    
    # Create buckets
    buckets = [[] for _ in range(num_buckets)]
    
    # Distribute elements into buckets
    for num in arr:
        # Map the number to a bucket index
        bucket_index = int(((num - min_val) / (max_val - min_val)) * (num_buckets - 1))
        buckets[bucket_index].append(num)
    
    # Sort individual buckets
    sorted_buckets = []
    for bucket in buckets:
        # Use Python's built-in sort for each bucket
        bucket.sort()
        sorted_buckets.extend(bucket)
    
    return sorted_buckets