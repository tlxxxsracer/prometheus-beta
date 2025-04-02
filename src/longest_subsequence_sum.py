def longest_subsequence_with_target_sum(arr, target):
    """
    Find the length of the longest subsequence where the sum of elements equals the target.
    
    Args:
        arr (list): Input list of integers
        target (int): Target sum to match
    
    Returns:
        int: Length of the longest subsequence with sum equal to target, 
             or 0 if no such subsequence exists
    
    Time Complexity: O(n^2)
    Space Complexity: O(n)
    """
    n = len(arr)
    
    # Edge cases
    if not arr:
        return 0
    
    # Initialize dynamic programming array to store max length for each sum
    max_length = 0
    
    # Nested loop to generate all possible subsequences
    for start in range(n):
        current_sum = 0
        current_length = 0
        
        for end in range(start, n):
            current_sum += arr[end]
            current_length += 1
            
            # Check if current subsequence matches target
            if current_sum == target:
                max_length = max(max_length, current_length)
            
            # Optimization: Stop if sum exceeds target
            if current_sum > target:
                break
    
    return max_length