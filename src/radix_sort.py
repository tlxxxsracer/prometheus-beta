def radix_sort(arr):
    """
    Implement the radix sort algorithm for sorting a list of non-negative integers.
    
    Radix sort is a non-comparative sorting algorithm that sorts integers by 
    processing individual digits from least significant to most significant digit.
    
    Args:
        arr (list): A list of non-negative integers to be sorted.
    
    Returns:
        list: A new sorted list of integers.
    
    Raises:
        TypeError: If the input is not a list or contains non-integer elements.
        ValueError: If any number in the list is negative.
    
    Time Complexity: O(d * (n + k)), where d is the number of digits, 
    n is the number of elements, and k is the range of input (10 for decimal)
    Space Complexity: O(n + k)
    """
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    if not arr:
        return []
    
    # Check for non-integer or negative elements
    if not all(isinstance(num, int) for num in arr):
        raise TypeError("All elements must be integers")
    
    if any(num < 0 for num in arr):
        raise ValueError("Radix sort only works with non-negative integers")
    
    # Find the maximum number to know the number of digits
    if not arr:
        return arr
    
    max_num = max(arr)
    
    # Do counting sort for every digit
    exp = 1
    while max_num // exp > 0:
        # Perform counting sort based on the current digit
        output = [0] * len(arr)
        count = [0] * 10
        
        # Store count of occurrences in count[]
        for i in range(len(arr)):
            index = arr[i] // exp
            count[index % 10] += 1
        
        # Change count[i] so that count[i] now contains actual
        # position of this digit in output[]
        for i in range(1, 10):
            count[i] += count[i - 1]
        
        # Build the output array
        i = len(arr) - 1
        while i >= 0:
            index = arr[i] // exp
            output[count[index % 10] - 1] = arr[i]
            count[index % 10] -= 1
            i -= 1
        
        # Copy the output array to arr[], so that arr[] now
        # contains sorted numbers according to current digit
        arr = output[:]
        
        # Move to next digit
        exp *= 10
    
    return arr