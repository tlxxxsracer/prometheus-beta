def convert_to_alternating_case(input_string):
    """
    Convert a string to alternating sentence case.

    This function transforms the input string so that consecutive letters alternate
    between uppercase and lowercase, starting with an uppercase letter.
    Non-letter characters do not affect the alternating pattern.

    Args:
        input_string (str): The input string to be converted.

    Returns:
        str: The string converted to alternating sentence case.

    Raises:
        TypeError: If the input is not a string.

    Examples:
        >>> convert_to_alternating_case("hello world")
        'HeLlO WoRlD'
        >>> convert_to_alternating_case("")
        ''
        >>> convert_to_alternating_case("a")
        'A'
    """
    # Check if input is a string
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")

    # If the string is empty, return empty string
    if not input_string:
        return ""

    # Convert to alternating case
    result = []
    letter_count = 0
    for char in input_string:
        if char.isalpha():
            # Alternate case based on letter count
            result.append(char.upper() if letter_count % 2 == 0 else char.lower())
            letter_count += 1
        else:
            # Non-letter characters remain unchanged
            result.append(char)

    return ''.join(result)