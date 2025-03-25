def compute_edit_distance(str1: str, str2: str) -> int:
    """
    Compute the minimum number of edits (insertions, deletions, or substitutions) 
    required to transform str1 into str2 using dynamic programming.

    Args:
        str1 (str): The source string
        str2 (str): The target string

    Returns:
        int: The minimum number of edits required

    Raises:
        TypeError: If inputs are not strings
    """
    # Type checking
    if not isinstance(str1, str) or not isinstance(str2, str):
        raise TypeError("Inputs must be strings")

    # Get lengths of input strings
    m, n = len(str1), len(str2)

    # Create a matrix to store edit distances
    # dp[i][j] will store the edit distance between str1[:i] and str2[:j]
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Initialize first row and column
    for i in range(m + 1):
        dp[i][0] = i  # Cost of deleting i characters from str1
    for j in range(n + 1):
        dp[0][j] = j  # Cost of inserting j characters into str1

    # Fill the dp table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # If characters are the same, no edit needed
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                # Minimum of insert, delete, or substitute
                dp[i][j] = 1 + min(
                    dp[i-1][j],      # deletion
                    dp[i][j-1],      # insertion
                    dp[i-1][j-1]     # substitution
                )

    # Return the bottom-right cell which contains the total edit distance
    return dp[m][n]