def find_unique_substrings(s: str) -> list[str]:
    """
    Find all unique substrings within the given string.
    
    Args:
        s (str): The input string to find unique substrings in
    
    Returns:
        list[str]: A list of unique substrings, sorted in lexicographic order
    
    Raises:
        TypeError: If the input is not a string
    
    Examples:
        >>> find_unique_substrings("abab")
        ['a', 'ab', 'aba', 'abab', 'b', 'ba', 'bab']
        >>> find_unique_substrings("")
        []
    """
    # Validate input
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    
    # If string is empty, return empty list
    if not s:
        return []
    
    # Find all unique substrings
    unique_substrings = set()
    
    # Generate all possible substrings
    for start in range(len(s)):
        for end in range(start + 1, len(s) + 1):
            unique_substrings.add(s[start:end])
    
    # Convert to sorted list
    return sorted(list(unique_substrings))