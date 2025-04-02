"""
LZ78 Compression Algorithm Implementation

This module provides functions for LZ78 compression and decompression.
LZ78 is a dictionary-based lossless compression algorithm that builds 
a dictionary of previously seen substrings during compression.
"""

def lz78_compress(input_string):
    """
    Compress the input string using LZ78 compression algorithm.
    
    Args:
        input_string (str): The string to be compressed
    
    Returns:
        list: A list of tuples (index, character) representing the compressed data
        
    Raises:
        TypeError: If input is not a string
        ValueError: If input is an empty string
    """
    # Input validation
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    if not input_string:
        raise ValueError("Input string cannot be empty")
    
    # Initialize dictionary and compressed output
    dictionary = {0: ''}  # 0 is reserved for empty string
    compressed = []
    current_dict_index = 1
    current_sequence = ''
    
    # Compress the input string
    for char in input_string:
        # Try to find the longest matching prefix in the dictionary
        current_sequence_with_char = current_sequence + char
        
        # Find if the current sequence with new char exists in dictionary
        found = False
        for index, value in dictionary.items():
            if value == current_sequence_with_char:
                current_sequence = current_sequence_with_char
                found = True
                break
        
        # If sequence not found, add to compressed output and update dictionary
        if not found:
            # Find the index of the current sequence before adding current char
            prev_index = 0
            for index, value in dictionary.items():
                if value == current_sequence:
                    prev_index = index
                    break
            
            # Add to compressed output and dictionary
            compressed.append((prev_index, char))
            dictionary[current_dict_index] = current_sequence_with_char
            current_dict_index += 1
            
            # Reset current sequence
            current_sequence = ''
    
    # Handle any remaining sequence
    if current_sequence:
        prev_index = 0
        for index, value in dictionary.items():
            if value == current_sequence:
                prev_index = index
                break
        compressed.append((prev_index, ''))
    
    return compressed

def lz78_decompress(compressed_data):
    """
    Decompress data that was compressed using LZ78 algorithm.
    
    Args:
        compressed_data (list): List of tuples (index, character) from compression
    
    Returns:
        str: The decompressed original string
        
    Raises:
        TypeError: If input is not a list
        ValueError: If compressed data is invalid
    """
    # Input validation
    if not isinstance(compressed_data, list):
        raise TypeError("Input must be a list of tuples")
    
    # Initialize dictionary and decompressed output
    dictionary = {0: ''}
    decompressed = []
    current_dict_index = 1
    
    # Decompress the input
    for index, char in compressed_data:
        # Validate input tuple
        if not isinstance(index, int) or not isinstance(char, str):
            raise ValueError(f"Invalid compressed data: {(index, char)}")
        
        # Retrieve the string from dictionary based on index
        if index not in dictionary:
            raise ValueError(f"Invalid dictionary index: {index}")
        
        # Construct current string
        current_string = dictionary[index] + char
        
        # Add to dictionary
        dictionary[current_dict_index] = current_string
        current_dict_index += 1
        
        # Add to decompressed output
        decompressed.append(current_string)
    
    # Join and return the decompressed string
    return ''.join(decompressed)