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
    
    # Special case: if original string is already a palindrome, return it
    if len(s) <= 1 or s == s[::-1]:
        return s
    
    # Count character frequencies
    char_counts = Counter(s)
    
    # Validate if palindrome is possible
    if not can_form_palindrome(s):
        return ''
    
    # Sort characters to ensure consistent output
    unique_chars = sorted(char_counts.keys())
    
    # Attempt to construct palindrome
    left_half = []
    center = ''
    
    for char in unique_chars:
        # Get count for this character
        count = char_counts[char]
        
        # Add pairs to left half
        left_half.extend([char] * (count // 2))
        
        # Find potential center character (the first one with odd count)
        if count % 2 != 0 and not center:
            center = char
    
    # Complete palindrome
    right_half = list(reversed(left_half))
    
    # Construct final palindrome
    return ''.join(left_half + ([center] if center else []) + right_half)