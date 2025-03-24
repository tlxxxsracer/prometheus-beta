def bitwise_and_range(m: int, n: int) -> int:
    """
    Calculate the bitwise AND of all numbers in the range [m, n] (inclusive).

    This function finds the bitwise AND of all integers from m to n by 
    identifying the common most significant bits while the numbers differ.

    Args:
        m (int): The lower bound of the range (inclusive)
        n (int): The upper bound of the range (inclusive)

    Returns:
        int: The bitwise AND of all numbers in the range

    Raises:
        ValueError: If m is greater than n or if either input is negative

    Examples:
        >>> bitwise_and_range(5, 7)
        4
        >>> bitwise_and_range(0, 1)
        0
    """
    # Validate input
    if m < 0 or n < 0:
        raise ValueError("Inputs must be non-negative integers")
    
    if m > n:
        raise ValueError("Lower bound must not be greater than upper bound")
    
    # If the range is empty or bounds are the same, return the bound
    if m == n:
        return m
    
    # Find the common most significant bits
    shift = 0
    while m != n:
        m >>= 1
        n >>= 1
        shift += 1
    
    # Shift back to get the common prefix
    return m << shift