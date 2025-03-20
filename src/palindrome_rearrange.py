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
    
    # Validate if palindrome is possible
    if not can_form_palindrome(s):
        return ''
    
    # Count character frequencies
    char_counts = Counter(s)
    
    # Prepare characters for palindrome
    chars = []
    middle = ''
    
    # Collect characters with even frequencies
    for char, count in sorted(char_counts.items()):
        # Add pairs of characters to the list
        chars.extend([char] * (count // 2))
        
        # Keep track of the character with odd frequency (if any)
        if count % 2 != 0:
            if not middle:
                middle = char
    
    # Construct palindrome
    left = chars
    right = list(reversed(chars))
    
    return ''.join(left + ([middle] if middle else []) + right)