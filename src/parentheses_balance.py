def is_balanced_parentheses(s: str) -> bool:
    """
    Check if a string of parentheses is balanced.
    
    A string of parentheses is considered balanced if:
    - Every opening parenthesis has a corresponding closing parenthesis
    - Parentheses are closed in the correct order
    
    Args:
        s (str): A string containing only parentheses characters
    
    Returns:
        bool: True if parentheses are balanced, False otherwise
    
    Raises:
        TypeError: If input is not a string or contains non-parentheses characters
    
    Examples:
        >>> is_balanced_parentheses("()")
        True
        >>> is_balanced_parentheses("((()))")
        True
        >>> is_balanced_parentheses("(())")
        True
        >>> is_balanced_parentheses(")(")
        False
        >>> is_balanced_parentheses("(()")
        False
        >>> is_balanced_parentheses("")
        True
    """
    # Validate input
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    
    # Check if string contains only parentheses
    if s and not all(char in '()' for char in s):
        raise TypeError("Input must contain only parentheses")
    
    # Use a stack to track opening parentheses
    stack = []
    
    # Iterate through each character in the input string
    for char in s:
        # If it's an opening parenthesis, push to stack
        if char == '(':
            stack.append(char)
        # If it's a closing parenthesis
        elif char == ')':
            # If stack is empty, no matching opening parenthesis
            if not stack:
                return False
            # Remove the last opening parenthesis
            stack.pop()
    
    # Stack should be empty for a perfectly balanced string
    return len(stack) == 0