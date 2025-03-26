def longest_palindromic_substring(s: str) -> str:
    """
    Find the longest palindromic substring in a given string.
    
    Args:
        s (str): Input string to search for palindromic substrings
    
    Returns:
        str: The longest palindromic substring
    
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    
    Edge Cases:
    - Empty string returns empty string
    - Single character is a palindrome
    - Multiple palindromes of same length returns first occurrence
    """
    # Handle edge cases
    if not s:
        return ""
    
    # Initialize variables to track longest palindrome
    start = 0
    max_length = 1
    
    def expand_around_center(left: int, right: int) -> int:
        """
        Expand around a center point to find palindrome length
        
        Args:
            left (int): Left index to start expanding
            right (int): Right index to start expanding
        
        Returns:
            int: Length of palindrome
        """
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        
        # Return length of palindrome (right - left - 1)
        return right - left - 1
    
    # Iterate through each character as potential center
    for i in range(len(s)):
        # Check odd length palindromes
        odd_length = expand_around_center(i, i)
        # Check even length palindromes
        even_length = expand_around_center(i, i + 1)
        
        # Update longest palindrome if current is longer
        current_max = max(odd_length, even_length)
        if current_max > max_length:
            # Calculate start index based on center and length
            start = i - (current_max - 1) // 2
            max_length = current_max
    
    # Return the longest palindromic substring
    return s[start:start + max_length]