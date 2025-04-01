from typing import List, Union

def log_array_table(arr: List[Union[str, int, float]], headers: List[str] = None) -> str:
    """
    Convert an array to a formatted table string.

    Args:
        arr (List[Union[str, int, float]]): The array to be logged.
        headers (List[str], optional): Custom headers for the table. 
                                       If not provided, uses default index headers.

    Returns:
        str: A formatted table representation of the array.

    Raises:
        TypeError: If input is not a list.
        ValueError: If headers do not match array length.
    """
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Handle empty list
    if not arr:
        return ''
    
    # If no headers provided, create default index headers
    if headers is None:
        headers = [str(i) for i in range(len(arr))]
    
    # Validate headers match array length
    if len(headers) != len(arr):
        raise ValueError("Number of headers must match array length")
    
    # Determine column width based on the longest string
    column_width = max(max(len(str(h)), len(str(v))) for h, v in zip(headers, arr)) + 2
    
    # Create table
    table_lines = []
    
    # Header line
    header_line = ' | '.join(header.ljust(column_width) for header in headers)
    table_lines.append(header_line)
    
    # Separator line with '-' characters matching the width of the header line
    separator_line = '-' * len(header_line)
    table_lines.append(separator_line)
    
    # Data line
    data_line = ' | '.join(str(item).ljust(column_width) for item in arr)
    table_lines.append(data_line)
    
    return '\n'.join(table_lines)