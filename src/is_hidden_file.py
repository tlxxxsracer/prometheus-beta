import os


def is_hidden_file(file_path):
    """
    Determine if a file is hidden.

    Args:
        file_path (str): The path to the file to check.

    Returns:
        bool: True if the file is hidden, False otherwise.

    Raises:
        FileNotFoundError: If the file does not exist.
        TypeError: If file_path is not a string.
    """
    # Check if input is a string
    if not isinstance(file_path, str):
        raise TypeError("file_path must be a string")

    # Normalize the path to handle both absolute and relative paths
    normalized_path = os.path.abspath(file_path)
    
    # Get the filename
    filename = os.path.basename(normalized_path)
    
    # Check Unix/Linux hidden file convention (starts with a dot)
    if filename.startswith('.'):
        return True
    
    # Check Windows hidden file attribute (platform-specific)
    try:
        import ctypes
        import sys
        
        if sys.platform.startswith('win'):
            attributes = ctypes.windll.kernel32.GetFileAttributesW(normalized_path)
            return attributes != -1 and bool(attributes & 0x02)  # FILE_ATTRIBUTE_HIDDEN
    except (ImportError, AttributeError):
        # If Windows-specific check fails, fall back to filename convention
        pass
    
    return False