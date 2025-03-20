from collections import Counter

def can_form_palindrome(s: str) -> bool:
    """
    Determine if the characters in the given string can be rearranged to form a palindrome.
    
    A palindrome can be formed if at most one character has an odd count.
    
    Args:
        s (str): Input string to check for palindrome rearrangement possibility
    
    Returns:
        bool: True if characters can be rearranged to form a palindrome, False otherwise
    
    Raises:
        TypeError: If input is not a string
    
    Examples:
        >>> can_form_palindrome("racecar")
        True
        >>> can_form_palindrome("hello")
        False
    """
    # Check input type
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    
    # Count character frequencies
    char_counts = Counter(s)
    
    # Count characters with odd frequencies
    odd_count = sum(1 for count in char_counts.values() if count % 2 != 0)
    
    # Palindrome is possible if at most one character has an odd count
    return odd_count <= 1

def rearrange_to_palindrome(s: str) -> str:
    """
    Rearrange characters in the given string to form a palindrome.
    
    Args:
        s (str): Input string to rearrange
    
    Returns:
        str: A palindrome formed by rearranging the input characters, 
             or an empty string if no palindrome is possible
    
    Raises:
        TypeError: If input is not a string
    
    Examples:
        >>> rearrange_to_palindrome("racecar")
        'racecar'
        >>> rearrange_to_palindrome("aab")
        'aba'
        >>> rearrange_to_palindrome("abc")
        ''
    """
    # Validate input
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    
    # Check if palindrome is possible
    if not can_form_palindrome(s):
        return ''
    
    # Count character frequencies
    char_counts = Counter(s)
    
    # Separate characters with even and odd counts
    even_chars = []
    odd_char = None
    
    # Build the palindrome
    for char, count in char_counts.items():
        if count % 2 == 0:
            # Add half of even count characters to both sides
            even_chars.extend([char] * (count // 2))
        else:
            # If no odd character found yet, use this one
            if odd_char is None:
                odd_char = char
            # Add half of the count to even characters
            even_chars.extend([char] * (count // 2))
    
    # Construct palindrome
    left = even_chars
    right = list(reversed(even_chars))
    middle = [odd_char] if odd_char is not None else []
    
    return ''.join(left + middle + right)