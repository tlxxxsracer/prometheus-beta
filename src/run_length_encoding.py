def run_length_encode(data):
    """
    Implement Run-Length Encoding (RLE) data compression.
    
    Args:
        data (str or list): Input data to be compressed
    
    Returns:
        list: Compressed data using Run-Length Encoding
    
    Raises:
        TypeError: If input is not a string or list
        ValueError: If input contains unsupported data types
    """
    # Handle empty input
    if not data:
        return []
    
    # Validate input type
    if not isinstance(data, (str, list)):
        raise TypeError("Input must be a string or list")
    
    # Compress the data
    compressed = []
    current_item = data[0]
    count = 1
    
    for item in data[1:]:
        if item == current_item:
            count += 1
        else:
            # Add the count and item to compressed result
            compressed.append((count, current_item))
            current_item = item
            count = 1
    
    # Add the last run
    compressed.append((count, current_item))
    
    return compressed

def run_length_decode(compressed_data):
    """
    Decompress data encoded using Run-Length Encoding.
    
    Args:
        compressed_data (list): List of (count, item) tuples
    
    Returns:
        list: Decompressed original data
    
    Raises:
        TypeError: If input is not a list of tuples
        ValueError: If tuple elements are invalid
    """
    # Handle empty input
    if not compressed_data:
        return []
    
    # Validate input
    if not isinstance(compressed_data, list):
        raise TypeError("Input must be a list of (count, item) tuples")
    
    # Validate each tuple
    if not all(isinstance(item, tuple) and len(item) == 2 
               and isinstance(item[0], int) and item[0] > 0 
               for item in compressed_data):
        raise TypeError("Input must be a list of valid (count, item) tuples")
    
    # Decompress the data
    decompressed = []
    for count, item in compressed_data:
        # Extend the decompressed list with repeated items
        decompressed.extend([item] * count)
    
    return decompressed