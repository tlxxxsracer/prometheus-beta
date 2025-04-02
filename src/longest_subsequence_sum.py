def longest_subsequence_with_target_sum(arr, target):
    """
    Find the length of the longest subsequence where the sum of elements equals the target.
    
    Args:
        arr (list): Input list of integers
        target (int): Target sum to match
    
    Returns:
        int: Length of the longest subsequence with sum equal to target, 
             or 0 if no such subsequence exists
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    n = len(arr)
    if not arr:
        return 0
    
    # Memoization to track the latest index for each cumulative sum
    sum_indices = {0: -1}
    current_sum = 0
    max_length = 0
    
    for i, num in enumerate(arr):
        current_sum += num
        
        # Check if there's a valid subsequence ending at current index
        if current_sum - target in sum_indices:
            current_length = i - sum_indices[current_sum - target]
            max_length = max(max_length, current_length)
        
        # Update the latest index for this cumulative sum
        # Always keep the leftmost index to maximize subsequence length
        if current_sum not in sum_indices:
            sum_indices[current_sum] = i
    
    return max_length