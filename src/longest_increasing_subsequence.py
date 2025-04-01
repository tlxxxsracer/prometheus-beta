def find_longest_increasing_subsequence(arr):
    """
    Find the longest increasing subsequence in the given array.
    
    Args:
        arr (list): Input list of integers
    
    Returns:
        list: The longest increasing subsequence
    
    Time Complexity: O(n^2)
    Space Complexity: O(n)
    
    Raises:
        TypeError: If input is not a list
        ValueError: If input list contains non-comparable elements
    """
    # Input validation
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    if not arr:
        return []
    
    # Validate elements are comparable
    try:
        sorted(arr)
    except TypeError:
        raise ValueError("List contains non-comparable elements")
    
    # Length of input array
    n = len(arr)
    
    # Dynamic programming arrays
    # longest[i] stores the length of LIS ending at index i
    longest = [1] * n
    
    # Stores the indices to reconstruct the subsequence
    prev_index = [-1] * n
    
    # Find the longest increasing subsequence
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j] and longest[i] < longest[j] + 1:
                longest[i] = longest[j] + 1
                prev_index[i] = j
    
    # Find the index of maximum length subsequence
    max_length_index = longest.index(max(longest))
    
    # Reconstruct the subsequence
    subsequence = []
    while max_length_index != -1:
        subsequence.insert(0, arr[max_length_index])
        max_length_index = prev_index[max_length_index]
    
    return subsequence