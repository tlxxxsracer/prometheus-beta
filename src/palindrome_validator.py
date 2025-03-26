def is_palindrome(s: str) -> bool:
    """
    Determine if a given string is a palindrome, ignoring spaces, 
    punctuation, and capitalization.
    
    Args:
        s (str): The input string to check
    
    Returns:
        bool: True if the string is a palindrome, False otherwise
    
    Raises:
        TypeError: If input is not a string
    
    Examples:
        >>> is_palindrome("A man, a plan, a canal: Panama")
        True
        >>> is_palindrome("race a car")
        False
        >>> is_palindrome("")
        True
    """
    # Validate input type
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    
    # Check if the cleaned string reads the same forwards and backwards
    return cleaned == cleaned[::-1]