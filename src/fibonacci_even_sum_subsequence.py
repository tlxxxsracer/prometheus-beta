def generate_fibonacci_subsequence(n):
    """
    Generate a Fibonacci subsequence where the sum of even-indexed numbers equals n.

    Args:
        n (int): The target sum of even-indexed numbers.

    Returns:
        list: A Fibonacci subsequence meeting the specified condition.

    Raises:
        ValueError: If n is negative or the subsequence cannot be generated.
    """
    # Handle invalid input
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    
    # Special case for 0
    if n == 0:
        return [0]
    
    # Try different starting points and lengths
    for start_index in range(10):  # More flexible search
        for length in range(2, 20):  # Reasonable length limit
            # Generate subsequence
            subsequence = [0, 1]
            while len(subsequence) < start_index + length:
                subsequence.append(subsequence[-1] + subsequence[-2])
            
            # Select subsequence and calculate even-indexed sum
            selected_subsequence = subsequence[start_index:start_index+length]
            even_sum = sum(selected_subsequence[::2])
            
            if even_sum == n:
                return selected_subsequence
    
    # If no subsequence found
    raise ValueError(f"No Fibonacci subsequence found with even-indexed sum of {n}")