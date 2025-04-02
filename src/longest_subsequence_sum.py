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
    # Cumulative sum tracking
    prefix_sums = {0: -1}  # Sum 0 at index -1
    current_sum = 0
    max_length = 0
    
    for i, num in enumerate(arr):
        current_sum += num
        
        # Check if current sum minus target exists in previous sums
        if current_sum - target in prefix_sums:
            max_length = max(max_length, i - prefix_sums[current_sum - target])
        
        # Store current sum's index, keeping the earliest occurrence
        if current_sum not in prefix_sums:
            prefix_sums[current_sum] = i
    
    return max_length