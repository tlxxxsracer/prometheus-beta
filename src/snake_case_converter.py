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
    
    # Replace hyphens and other non-word characters with spaces
    cleaned_string = re.sub(r'[^a-zA-Z0-9]+', ' ', input_string)
    
    # Complex regex to capture camel/pascal case, including numbers
    words = re.findall(r'[A-Z0-9]+(?=[A-Z][a-z]+|\d|\W|$)|[a-z]+\d*|\d+|[A-Z][a-z]+', cleaned_string)
    
    # Convert to lowercase and join with underscore
    snake_case_words = [w.lower() for w in words]
    
    # If no words were found, convert the original string to lowercase
    return '_'.join(snake_case_words) if snake_case_words else input_string.lower()