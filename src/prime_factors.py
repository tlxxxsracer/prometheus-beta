def get_prime_factors(n: int) -> list[int]:
    """
    Calculate the prime factors of a positive integer in ascending order.

    Args:
        n (int): A positive integer to factorize.

    Returns:
        list[int]: A sorted list of prime factors.

    Raises:
        ValueError: If the input is not a positive integer.
    """
    # Validate input
    if not isinstance(n, int):
        raise ValueError("Input must be an integer")
    
    if n <= 0:
        raise ValueError("Input must be a positive integer")
    
    # Special case for 1
    if n == 1:
        return []
    
    # Initialize list to store prime factors
    factors = []
    
    # Start with the smallest prime number
    divisor = 2
    
    # Find prime factors
    while divisor * divisor <= n:
        # If divisor divides n completely
        if n % divisor == 0:
            # Add divisor to factors
            factors.append(divisor)
            # Divide n by divisor
            n //= divisor
        else:
            # Move to next potential divisor
            divisor += 1
    
    # If n is greater than 1, it is a prime factor itself
    if n > 1:
        factors.append(n)
    
    return factors