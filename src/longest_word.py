def find_longest_word(sentence):
    """
    Find the longest word in a given sentence.

    Args:
        sentence (str): The input sentence to search for the longest word.

    Returns:
        str: The longest word in the sentence. If multiple words have the same 
             maximum length, returns the first occurrence.

    Raises:
        TypeError: If the input is not a string.
        ValueError: If the input string is empty or contains only whitespace.
    """
    # Check input type
    if not isinstance(sentence, str):
        raise TypeError("Input must be a string")
    
    # Remove leading/trailing whitespace and check if empty
    sentence = sentence.strip()
    if not sentence:
        raise ValueError("Input sentence cannot be empty")
    
    # Split the sentence into words, handling multiple whitespaces
    words = sentence.split()
    
    # If no words after splitting, raise ValueError
    if not words:
        raise ValueError("No words found in the sentence")
    
    # Return the longest word (first occurrence in case of ties)
    return max(words, key=len)