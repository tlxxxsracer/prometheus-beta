import re

def to_snake_case(input_string: str) -> str:
    """
    Convert a given string to snake_case.
    
    This function handles various input formats including:
    - Camel Case
    - Pascal Case
    - Kebab Case
    - Space-separated words
    - Mixed case strings
    
    Args:
        input_string (str): The input string to convert to snake case
    
    Returns:
        str: The converted snake_case string
    
    Raises:
        TypeError: If input is not a string
    
    Examples:
        >>> to_snake_case("HelloWorld")
        'hello_world'
        >>> to_snake_case("hello-world")
        'hello_world'
        >>> to_snake_case("Hello World")
        'hello_world'
        >>> to_snake_case("helloWorld")
        'hello_world'
    """
    # Check if input is a string
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Handle empty string
    if not input_string:
        return ""
    
    # Replace non-alphanumeric characters with space
    cleaned_string = re.sub(r'[^a-zA-Z0-9]+', ' ', input_string)
    
    # Insert underscores between lowercase and uppercase letters 
    # and between letters and numbers
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', cleaned_string)
    s2 = re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1)
    
    # Remove leading/trailing spaces, convert to lowercase
    # Replace multiple spaces with single underscore
    snake_case = re.sub(r'\s+', '_', s2).lower().strip('_')
    
    # Handle single character case
    return snake_case if snake_case else input_string.lower()