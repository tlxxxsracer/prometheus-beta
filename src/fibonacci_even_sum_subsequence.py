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
    
    # Try different subsequence lengths
    for length in range(2, 20):  # Reasonable length limit
        # Initialize subsequence with first two Fibonacci numbers
        subsequence = [0, 1]
        
        # Generate subsequence
        while len(subsequence) < length:
            subsequence.append(subsequence[-1] + subsequence[-2])
        
        # Check if sum of even-indexed numbers matches target
        even_sum = sum(subsequence[::2])
        
        if even_sum == n:
            return subsequence
    
    # If no subsequence found
    raise ValueError(f"No Fibonacci subsequence found with even-indexed sum of {n}")