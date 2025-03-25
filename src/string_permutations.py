def generate_unique_permutations(s: str) -> list[str]:
    """
    Generate all possible unique permutations of a given string.
    
    Args:
        s (str): Input string to generate permutations for
    
    Returns:
        list[str]: A list of unique permutations of the input string
    
    Raises:
        TypeError: If input is not a string
    
    Examples:
        >>> generate_unique_permutations("abc")
        ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
        >>> generate_unique_permutations("aba")
        ['aba', 'aab', 'baa']
    """
    # Validate input
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    
    # Handle empty string case
    if not s:
        return []
    
    # Convert to list for easier manipulation
    chars = list(s)
    
    # Use a set to ensure unique permutations
    unique_perms = set()
    
    def backtrack(start: int):
        """
        Recursive backtracking to generate permutations
        
        Args:
            start (int): Starting index for current permutation generation
        """
        # Base case: if we've reached the end of the string
        if start == len(chars):
            unique_perms.add(''.join(chars))
            return
        
        # Generate permutations
        for i in range(start, len(chars)):
            # Swap characters
            chars[start], chars[i] = chars[i], chars[start]
            
            # Recurse
            backtrack(start + 1)
            
            # Backtrack (undo the swap)
            chars[start], chars[i] = chars[i], chars[start]
    
    # Start the permutation generation
    backtrack(0)
    
    # Convert to sorted list for consistent output
    return sorted(list(unique_perms))