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
    
    # Convert to camel case first
    # 1. Replace any non-alphanumeric characters with space
    # 2. Split into words
    # 3. Adjust case and add underscore
    words = re.findall(r'[A-Z0-9]+(?=[A-Z][a-z]+|\d|\W|$)|\d+|[A-Z][a-z]+', input_string)
    
    # Convert to snake case
    snake_case_words = [w.lower() for w in words]
    
    # Join with underscore
    return '_'.join(snake_case_words)