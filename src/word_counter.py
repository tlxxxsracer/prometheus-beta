def count_words(text: str) -> int:
    """
    Count the number of words in a given string.

    Args:
        text (str): The input string to count words from.

    Returns:
        int: The number of words in the string.

    Notes:
        - Words are defined as sequences of non-whitespace characters
        - Leading, trailing, and multiple whitespaces are handled
        - Empty string or string with only whitespace returns 0
    """
    # Handle None or non-string input
    if text is None:
        return 0
    
    # Convert to string to handle potential non-string inputs
    text = str(text)
    
    # Strip leading and trailing whitespace and split on whitespace
    # Use split() without arguments to handle multiple whitespace characters
    words = text.strip().split()
    
    return len(words)