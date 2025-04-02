def find_longest_substring(s: str) -> str:
    """
    Find the longest substring without repeating characters.
    
    Args:
        s (str): Input string to search for the longest unique substring
    
    Returns:
        str: The longest substring without repeating characters
             If multiple such substrings exist, returns the first one
    
    Examples:
        >>> find_longest_substring("abcabcbb")
        'abc'
        >>> find_longest_substring("bbbbb")
        'b'
        >>> find_longest_substring("")
        ''
    """
    # Handle empty string edge case
    if not s:
        return ""
    
    # Initialize variables to track the longest substring
    longest_substring = ""
    current_substring = ""
    
    for char in s:
        # If character is not in current substring, add it
        if char not in current_substring:
            current_substring += char
        else:
            # If character is repeated, update longest substring if needed
            if len(current_substring) > len(longest_substring):
                longest_substring = current_substring
            
            # Slide the window to remove repeated characters
            current_substring = current_substring[current_substring.index(char) + 1:] + char
    
    # Final check after processing all characters
    if len(current_substring) > len(longest_substring):
        longest_substring = current_substring
    
    return longest_substring